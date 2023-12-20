from django.db import models
from django.utils import timezone
from rest_framework.authtoken.models import Token

class CustomToken(Token):
    date_expiration = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=1))

    def is_expired(self):
        return self.date_expiration < timezone.now()
