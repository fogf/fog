from .serializers import *
from fog.utils.restful_api import viewsets


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class CelebrityViewSet(viewsets.ModelViewSet):
    queryset = Celebrity.objects.all()
    serializer_class = CelebritySerializer