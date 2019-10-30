from django.db import models

class Cliente(models.Model):
    nome = models.DateTimeField()
    telefone = models.IntegerField()

    def __str__(self):
        return self.nome
