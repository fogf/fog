from .models import *
from rest_framework import serializers

class CelebritySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Celebrity
        fields = '__all__'

class MovieSerializer(serializers.HyperlinkedModelSerializer):

    directors = CelebritySerializer(many=True, read_only=True)
    scriptwriters = CelebritySerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

class CelebritySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Celebrity
        fields = '__all__'

