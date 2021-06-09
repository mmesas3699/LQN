import graphene
from graphene.types.scalars import String

from characters.models import Character, Movie, Planet
from characters.types import CharacterType, MovieType, PlanetType

 
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

            return None
        
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
        movie_id = graphene.ID()
        characters = graphene.List(String, description="List of character's names")
    
    movie = graphene.Field(MovieType)

    def mutate(self, info, movie_id, characters):
        movie_instance = Movie.objects.get(id=movie_id)
        if characters:
            for character in characters:
                character_instance = Character.objects.get(name=character)
                movie_instance.characters.add(character_instance)
            
            return AddCharactersToMovie(movie=movie_instance)
        else:
            return None


class AddPlanetsToMovie(graphene.Mutation):
    class Arguments:
        movie_id = graphene.ID()
        planets = graphene.List(String, description="List of planet's names")

    movie = graphene.Field(MovieType)

    def mutate(self, info, movie_id, planets):
        movie_instance = Movie.objects.get(id=movie_id)
        if planets:
            for planet in planets:
                planet_instance = Planet.objects.get(name=planet)
                movie_instance.planets.add(planet_instance)
            
            return AddPlanetsToMovie(movie=movie_instance)
        else:
            return None


class UpdateMovie(graphene.Mutation):
    class Arguments:
        movie_id = graphene.ID()
        name = graphene.String()
        year = graphene.Int()
        opening_text = graphene.String()
        director_name = graphene.String()
    
    movie = graphene.Field(MovieType)

    def mutate(self, info, movie_id, name, year, opening_text, director_name):
        movie_instance = Movie.objects.get(id=movie_id)
        if movie_instance:
            movie_instance.name = name
            movie_instance.year = year
            movie_instance.opening_text = opening_text
            movie_instance.director = director_name
            movie_instance.save()

            return UpdateMovie(movie=movie_instance)
        else:
            return None


class DeleteMovie(graphene.Mutation):
    class Arguments:
        movie_id = graphene.ID()
    
    movie = graphene.Field(MovieType)

    def mutate(self, info, movie_id):
        movie_instance = Movie.objects.get(id=movie_id)
        if movie_instance:
            movie_instance.delete()

            return None
        else:
            return None


class CreatePlanet(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    planet = graphene.Field(PlanetType)

    def mutate(self, info, name):
        planet_instance = Planet.objects.create(name=name)

        return CreatePlanet(planet=planet_instance)


class UpdatePlanet(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
    
    planet = graphene.Field(PlanetType)

    def mutate(self, info, id, name):
        planet_instance = Planet.objects.get(id=id)
        if planet_instance:
            planet_instance.name = name
            planet_instance.save()

            return UpdatePlanet(planet=planet_instance)
        else:
            return None


class DeletePlanet(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    planet = graphene.Field(PlanetType)

    def mutate(self, info, id):
        planet_instance = Planet.objects.get(id=id)
        if planet_instance:
            planet_instance.delete()
            return None
        else:
            return None