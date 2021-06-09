import graphene

import characters.querys 
from characters import mutations


class Query(characters.querys.Query, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    create_character = mutations.CreateCharacter.Field()
    update_character = mutations.UpdateCharacter.Field()
    delete_character = mutations.DeleteCharacter.Field()

    create_movie = mutations.CreateMovie.Field()
    update_movie = mutations.UpdateMovie.Field()
    delete_movie = mutations.DeleteMovie.Field()
    add_characters_movie = mutations.AddCharactersToMovie.Field()
    add_planets_movie = mutations.AddPlanetsToMovie.Field()

    create_planet = mutations.CreatePlanet.Field()
    update_planet = mutations.UpdatePlanet.Field()
    delete_planet = mutations.DeletePlanet.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
