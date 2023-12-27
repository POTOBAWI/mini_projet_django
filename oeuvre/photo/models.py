from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.contrib.auth import get_user_model

class Utilisateur(AbstractUser):
    email = models.EmailField(unique=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date_naissance = models.DateField(null=True,blank=True)
    role = models.CharField(max_length=20, choices=[('abonne', 'Abonné'), ('createur', 'Créateur'), ('administrateur', 'Administrateur')])

    # Ajoutez d'autres champs personnalisés si nécessaire

    def __str__(self):
        return self.email
# models.py
from django.db import models
from .models import Utilisateur

class Publication(models.Model):
    createur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='publications/')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
    # models.py
from django.db import models
from django.contrib.auth import get_user_model

Utilisateur = get_user_model()

class Suivi(models.Model):
    suiveur = models.ForeignKey(Utilisateur, related_name='suiveurs', on_delete=models.CASCADE)
    suivi = models.ForeignKey(Utilisateur, related_name='suivis', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('suiveur', 'suivi')

# models.py


Utilisateur = get_user_model()

class Commentaire(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    createur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
