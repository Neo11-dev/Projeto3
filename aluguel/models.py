from django.db import models

class Aluguel(models.Model):
    data_festa = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    valor_cobrado = models.IntegerField()

    def __str__(self):
        return self.data_festa
