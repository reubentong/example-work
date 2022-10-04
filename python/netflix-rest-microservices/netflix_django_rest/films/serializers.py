from rest_framework import serializers
from .models import Film


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film  # this is the model that is being serialized
        fields = ('film_title', 'director', 'blurb', 'genre', 'added_on')
