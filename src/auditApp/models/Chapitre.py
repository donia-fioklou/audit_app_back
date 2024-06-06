from django.db import models

from auditApp.models.Annexe import Annexe



class Chapitre(models.Model):
    annexeA = models.ForeignKey(Annexe, on_delete=models.CASCADE)
    numero = models.TextField(default='')
    nom = models.TextField()
    NoteCible = models.IntegerField(default=0)
    #conformite = models.FloatField(default=0)  # pourcentage de conformite
    #veracite = models.IntegerField(default=0)  # nombre de veracite
    #status = models.IntegerField()

    class Meta:
        verbose_name = 'Chapitre'
        verbose_name_plural = 'Chapitres'
    def __str__(self):
        return self.nom
