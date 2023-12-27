# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur



from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Email')

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']



class CustomRegistrationForm(UserCreationForm):
    date_naissance = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=True)

    class Meta:
        model = Utilisateur
        fields = ['email', 'nom', 'prenom', 'date_naissance', 'password1', 'password2']
# forms.py
from django import forms
from .models import Publication

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['titre', 'description', 'image']
# forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Utilisateur

class MiseAJourProfilForm(UserChangeForm):
    class Meta:
        model = Utilisateur
        fields = ['email', 'nom', 'prenom', 'date_naissance']
        # forms.py
from django import forms
from .models import Commentaire

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']


