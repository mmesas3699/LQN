import graphene

from graphene_django import DjangoObjectType

from characters.models import Character, Movie, Planet
from characters.types import CharacterType, MovieType, PlanetType


class Query(graphene.ObjectType):
    characters = graphene.List(CharacterType)
    character = graphene.Field(CharacterType, name=graphene.String())
    movies = graphene.List(MovieType)
    planets = graphene.List(PlanetType)

    def resolve_characters(self, info):
        return Character.objects.all()

    def resolve_character(self, info, name):
        return Character.objects.get(name=name)

    def resolve_movies(self, info):
        return Movie.objects.all()
    
    def resolve_planets(self, info):
        return Planet.objects.all()
