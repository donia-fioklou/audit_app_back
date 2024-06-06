from django.db import models

from auditApp.models.Chapitre import Chapitre
from auditApp.models.Annexe import Annexe


class SousChapitre(models.Model):
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE,related_name='chapitre')
    numero = models.TextField(default='')
    nom = models.TextField()
    #conformite = models.FloatField(default=0)  # pourcentage de conformite
    #veracite = models.IntegerField(default=0)  # nombre de veracite
    #status = models.IntegerField()

    class Meta:
        verbose_name = 'SousChapitre'
        verbose_name_plural = 'SousChapitres'
    
    def __str__(self):
        return self.nom
