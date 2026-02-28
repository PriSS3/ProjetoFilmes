
from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    ano = models.IntegerField()
    sinopse = models.TextField()

def str(self):
 return self.titulo



