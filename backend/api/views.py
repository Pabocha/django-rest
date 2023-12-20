
from django.shortcuts import render
from django.http import JsonResponse

from django.utils import timezone
from datetime import timedelta
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .models import CustomToken

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            # Vérifiez si l'utilisateur a un token existant et s'il est expiré
            try:
                token = CustomToken.objects.get(user=user)
                if token.is_expired():
                    token.delete()
                    token = CustomToken.objects.create(user=user)
                    token.date_expiration = timezone.now() + timedelta(days=1)  # Définir la nouvelle date d'expiration
                    token.save()
            except CustomToken.DoesNotExist:
                token = CustomToken.objects.create(user=user)
                token.date_expiration = timezone.now() + timedelta(days=1)  # Définir la date d'expiration initiale
                token.save()

            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def app_view(request, *args, **kwargs):
    data = {
        'name': 'donald',
        'language': 'python',
        'framework': 'Django',
    }
    return JsonResponse(data)


