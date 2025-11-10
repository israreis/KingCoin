from django.contrib.auth.models import User
from django.db import models
import os

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='profile'
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Telefone"
    )
    photo = models.ImageField(
        upload_to='profile_photos/',
        null=True,
        blank=True,
        verbose_name="Foto de perfil"
    )
    
    def __str__(self):
        return f"Perfil de {self.user.email}"
    
    def delete(self, *args, **kwargs):
        # Deleta a foto do sistema de arquivos quando o perfil é deletado
        if self.photo:
            if os.path.isfile(self.photo.path):
                os.remove(self.photo.path)
        super().delete(*args, **kwargs)