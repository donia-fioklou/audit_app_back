from django.db import models

class Exigence(models.Model):
    nom = models.CharField(max_length=100)
    #status = models.IntegerField()
    
    class Meta:
        verbose_name = 'Exigence'
        verbose_name_plural = 'Exigences'