

# Create your views here.
# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomAuthenticationForm,CustomRegistrationForm

# accueil ici
def accueil(request):
    return render(request,"accueil.html")
# fonction de connexion
# views.py
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'  # Assurez-vous que le nom de votre template de connexion est correct

def inscription_view(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accueil')
    else:
        form = CustomRegistrationForm()

    return render(request, 'inscription.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PublicationForm

 # pour s'assurer que l'utilisateur est connecté pour accéder à cette vue
def creation_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.createur = request.user  # Assigne le créateur de la publication à l'utilisateur connecté
            publication.save()
            return redirect('accueil')  # Redirigez vers la page d'accueil ou une autre page après la création de la publication
    else:
        form = PublicationForm()

    return render(request, 'creation_publication.html', {'form': form})
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Suivi

@login_required
def suivre_utilisateur(request, utilisateur_id):
    utilisateur_a_suivre = get_object_or_404(User, id=utilisateur_id)
    suivi, created = Suivi.objects.get_or_create(suiveur=request.user, suivi=utilisateur_a_suivre)
    if created:
        message = "Vous suivez maintenant {}".format(utilisateur_a_suivre.username)
    else:
        suivi.delete()
        message = "Vous ne suivez plus {}".format(utilisateur_a_suivre.username)
    return JsonResponse({'message': message})


from django.shortcuts import render
from django.http import HttpResponseForbidden

def liste_suivis(request):
    # Vérifier si l'utilisateur est authentifié
    if not request.user.is_authenticated:
        # Si l'utilisateur n'est pas authentifié, vous pouvez rediriger vers une page de connexion ou renvoyer une réponse appropriée.
        return HttpResponseForbidden("Vous devez être connecté pour accéder à cette page.")

    # Utiliser l'utilisateur authentifié pour récupérer les objets Suivi
    suivis = Suivi.objects.filter(suiveur=request.user)
    return render(request, 'liste_suivis.html', {'suivis': suivis})

# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Suivi, Publication

@login_required
def flux_social(request):
    suivis = Suivi.objects.filter(suiveur=request.user)
    utilisateurs_suivis = [suivi.suivi for suivi in suivis]
    publications_flux = Publication.objects.filter(createur__in=utilisateurs_suivis).order_by('-date_creation')
    return render(request, 'flux_social.html', {'publications_flux': publications_flux})
# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Publication

@login_required
def posts_utilisateur(request):
    publications_utilisateur = Publication.objects.filter(createur=request.user).order_by('-date_creation')
    return render(request, 'posts_utilisateur.html', {'publications_utilisateur': publications_utilisateur})
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MiseAJourProfilForm

@login_required
def mise_a_jour_profil(request):
    if request.method == 'POST':
        form = MiseAJourProfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accueil')  # Redirigez vers la page d'accueil ou une autre page après la mise à jour du profil
    else:
        form = MiseAJourProfilForm(instance=request.user)

    return render(request, 'mise_a_jour_profil.html', {'form': form})
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CommentaireForm
from .models import Commentaire
from django.views import View

@login_required
def ajouter_commentaire(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)

    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.publication = publication
            commentaire.createur = request.user
            commentaire.save()
            return redirect('accueil')  # Redirigez vers la page d'accueil ou la publication après l'ajout du commentaire
    else:
        form = CommentaireForm()

    return render(request, 'ajouter_commentaire.html', {'form': form, 'publication': publication})
from django.shortcuts import render
from .models import Utilisateur,Publication  # Assurez-vous de remplacer 'VotreModele' par le nom de votre modèle

def liste_elements(request):
    elements = Utilisateur.objects.all()  # Récupère tous les éléments de la base de données
    return render(request, 'liste_elements.html', {'elements': elements})
class PublicationDetailView(View):
    template_name = 'publication_detail.html'

    def get(self, request, *args, **kwargs):
        publication_id = kwargs.get('publication_id')
        publication = Publication.objects.get(id=publication_id)
        return render(request, self.template_name, {'publication': publication})

