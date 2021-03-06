from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero


# Create your views here.

class HeroViewset(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('age')
    serializer_class = HeroSerializer
