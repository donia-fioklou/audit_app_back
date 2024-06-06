from django.db import models
from .SousChapitre import SousChapitre
class ReponseSousChapitre(models.Model):
    sous_chapitre = models.ForeignKey(SousChapitre, on_delete=models.CASCADE)
    point = models.IntegerField()
    #date created
    date = models.DateField(auto_now_add=True)
    