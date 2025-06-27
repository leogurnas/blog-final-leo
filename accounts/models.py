from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
