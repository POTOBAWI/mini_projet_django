"""
URL configuration for oeuvre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from photo.views import PublicationDetailView, liste_elements,ajouter_commentaire,posts_utilisateur,mise_a_jour_profil, CustomLoginView,accueil,inscription_view, creation_publication,liste_suivis,flux_social
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscription/',inscription_view,name="inscription"),
    path('publication/', creation_publication,name='publication'),
    path('login/', CustomLoginView.as_view(),name='login'),
    path('', accueil,name='accueil'),
    path('liste_suivis/', liste_suivis,name='liste_suivis'),
    path('mise_a_jour/', mise_a_jour_profil,name='mise_a_jour_profil'),
    path('post/', posts_utilisateur,name='posts_utilisateur'),
    path('ajouter_commentaire/<int:publication_id>/',ajouter_commentaire, name='ajouter_commentaire'),
    





    
    path('publication/<int:publication_id>/', PublicationDetailView.as_view(), name='publication_detail'),


]
# urls.py



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

