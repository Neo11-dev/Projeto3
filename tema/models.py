from django.db import models

class Tema(models.Model):
    nome = models.CharField(max_length=100)
    valor_aluguel = models.IntegerField()
    cor_toalha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


