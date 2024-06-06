from django.db import models

from auditApp.models.Exigence import Exigence


class Article(models.Model):
    exigence = models.ForeignKey(Exigence, on_delete=models.CASCADE)
    nom = models.TextField()
    conformite = models.FloatField(default=0)  # pourcentage de conformite
    veracite = models.IntegerField(default=0)  # nombre de veracite
    #status = models.IntegerField()

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
