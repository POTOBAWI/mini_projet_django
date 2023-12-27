from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from .models import Utilisateur, Publication, Suivi

admin.site.register(Utilisateur)
admin.site.register(Publication)
admin.site.register(Suivi)

