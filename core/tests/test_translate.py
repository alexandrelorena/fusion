# models.py
from django.db import models

class Recurso(models.Model):
    recurso = models.CharField(max_length=100)
    descricao = models.TextField(max_length=200)

    def __str__(self):
        return self.recurso
