from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from .models import CustomToken  # Importez votre modèle personnalisé

class CustomTokenAdmin(TokenAdmin):
    list_display = ('key', 'user', 'created', 'date_expiration')  # Ajoutez 'date_expiration' à la liste des champs à afficher
    fields = ('user', 'date_expiration')

# Enregistrez votre CustomTokenAdmin avec le modèle CustomToken
# admin.site.unregister()  # Désenregistrez le modèle Token par défaut
admin.site.register(CustomToken, CustomTokenAdmin)  # Enregistrez le modèle CustomToken avec votre personnalisation
