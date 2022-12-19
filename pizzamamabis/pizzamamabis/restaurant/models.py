from django.db import models

class Restaurant(models.Model):
    nom = models.CharField(max_length=200)
    rue = models.CharField(max_length=400)
    code_postal = models.FloatField(default=0)
    ville = models.CharField(max_length=200)


    def __str__(self):
        return self.nom
