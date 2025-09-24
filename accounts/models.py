from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Utilisateur personnalisé pour l'application Gabon Citoyen"""
    
    LOCATION_CHOICES = [
        ('gabon', 'Gabon'),
        ('diaspora', 'Diaspora'),
    ]
    
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES, default='gabon')
    birth_date = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    circonscription = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
