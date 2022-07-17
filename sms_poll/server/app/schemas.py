from typing import Generic, TypeVar

from pydantic.generics import GenericModel
from tortoise.contrib.pydantic import PydanticModel, pydantic_model_creator

from .models import Items, Votes, Settings

T = TypeVar('T')

ItemsInSchema = pydantic_model_creator(Items, name='ItemsIn', exclude=['id'])
ItemsSchema = pydantic_model_creator(Items, name='Items')

class VotesSchema(pydantic_model_creator(Votes, name='Votes')):
    item_id: int

class VotesInSchema(pydantic_model_creator(Votes, name='VotesIn', exclude=['id'])):
    item_id: int

class SettingsInSchema(PydanticModel, GenericModel, Generic[T]):
    name: str
    value: T

    class Config:
        orig_model = Settings
        
class SettingsSchema(SettingsInSchema, GenericModel, Generic[T]):
    type: str
