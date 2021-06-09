import graphene

import characters.querys 
from characters import mutations


class Query(characters.querys.Query, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    create_character = mutations.CreateCharacter.Field()
    update_character = mutations.UpdateCharacter.Field()
    delete_character = mutations.DeleteCharacter.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
