import graphene

from characters.models import Character
from characters.types import CharacterType

 
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
