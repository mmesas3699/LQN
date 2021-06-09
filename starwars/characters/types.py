import graphene

from graphene_django import DjangoObjectType

from characters.models import Character, Movie, Planet


class CharacterType(DjangoObjectType):
    class Meta:
        model = Character
        fields = ('id', 'name', 'movies')


class PlanetType(DjangoObjectType):
    class Meta:
        model = Planet
        fields = ('id', 'name', 'movies')


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        fields = (
            'id', 'name', 'year', 'opening_text', 'director_name',
            'planets', 'characters')
