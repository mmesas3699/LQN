import graphene
from graphene.types.scalars import String

from characters.models import Character, Movie, Planet
from characters.types import CharacterType, MovieType

 
class CreateCharacter(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    character = graphene.Field(CharacterType)

    def mutate(self, info, name):
        character_instance = Character(
            name=name
        )
        character_instance.save()
        return CreateCharacter(character=character_instance)


class UpdateCharacter(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
    
    character = graphene.Field(CharacterType)

    def mutate(self, info, id, name):
        character_instance = Character.objects.get(id=id)

        if character_instance:
            character_instance.name = name
            character_instance.save()

            return UpdateCharacter(character=character_instance)
        
        return UpdateCharacter(character=character_instance)


class DeleteCharacter(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    character = graphene.Field(CharacterType)

    def mutate(self, info, id):
        character_instance = Character.objects.get(id=id)

        if character_instance:
            character_instance.delete()

            return DeleteCharacter(character=character_instance)
        
        return None


class CreateMovie(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        year = graphene.Int()
        opening_text = graphene.String()
        director = graphene.String()
        planets = graphene.List(String, description="List of planet's names")
        characters = graphene.List(String)

    movie = graphene.Field(MovieType)

    def mutate(self, info, name, year, opening_text, director, planets, characters):
        movie = Movie.objects.create(
            name=name,
            year=year,
            opening_text=opening_text,
            director_name=director,
        )
        if planets:
            for planet in planets:
                planet_instance = Planet.objects.get(name=planet)
                movie.planets.add(planet_instance)
        
        if characters:
            for character in characters:
                character_instance = Character.objects.get(name=character)
                movie.characters.add(character_instance)
        
        return CreateMovie(movie=movie)


class AddCharactersToMovie(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        characters = graphene.List(String, description="List of character's names")
    
    movie = graphene.Field(MovieType)

    def mutate(self, info, id, characters):
        movie_instance = Movie.objects.get(id=id)
        if characters:
            for character in characters:
                character_instance = Character.objects.get(name=character)
                movie_instance.characters.add(character_instance)
            
            return AddCharactersToMovie(movie=movie_instance)
        else:
            return None


class AddPlanetsToMovies(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        planets = graphene.List(String, description="List of planet's names")

    movie = graphene.Field(MovieType)

    def mutate(self, info, id, planets):
        movie_instance = Movie.objects.get(id=id)
        if planets:
            for planet in planets:
                planet_instance = Planet.objects.get(name=planet)
                movie_instance.planets.add(planet_instance)
            
            return AddPlanetsToMovies(movie=movie_instance)
        else:
            return None
