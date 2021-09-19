from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField('Primeiro nome', max_length=70, blank=True)
    last_name = models.CharField('Último nome',max_length=70, blank=True)
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    image = models.ImageField(default='default.png',
                              upload_to='profile_images')

    def __str__(self):
        return f'{self.customer.username}-Perfil'
    
    
    class Meta :
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"