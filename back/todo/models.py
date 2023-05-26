from django.db import models

class Tarefa(models.Model):
    nome = models.CharField(max_length=256)
    descricao = models.CharField(max_length=256, default="", blank=True, null=True)
    def __str__(self):
        return (self.nome)