from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import TarefaSerializer
from .models import Tarefa

class TarefaViewSet(ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer