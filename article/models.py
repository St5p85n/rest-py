from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Produit(models.Model):
    libelle = models.CharField(max_length=100)
    quantite = models.IntegerField()
    prix = models.FloatField()
    dateCreation = models.DateField(auto_now_add=True)

class Utilisateur(AbstractUser):
    telephone = models.CharField(max_length=11)
    adresse = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='utils', blank=True)