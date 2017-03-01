from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer