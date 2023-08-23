from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class login(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
   

   
   
