from django.db import models

class Annexe(models.Model):
    nom = models.CharField(max_length=100)
    #status = models.IntegerField()
    class Meta:
        verbose_name = 'Annexe'
        verbose_name_plural = 'Annexes'
    
    def __str__(self):
        return self.nom
    