# from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TechniquesSerializer
from .models import Techniques

class TechniquesViewSet(viewsets.ModelViewSet):
    queryset = Techniques.objects.all().order_by('name')
    serializer_class = TechniquesSerializer