from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class login(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    titre = models.CharField(max_length=100, default="si")
    def __str__(self):
        return self.titre  


   

class Video(models.Model):
    titre = models.CharField(max_length=100)
    lien = models.URLField(blank=True)
    
    def __str__(self):
        return self.titre   

   
   
