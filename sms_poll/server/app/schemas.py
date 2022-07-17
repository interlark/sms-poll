from typing import Generic, TypeVar, Any

from pydantic.generics import GenericModel
from tortoise.contrib.pydantic import PydanticModel, pydantic_model_creator

from .models import Items, Votes, Settings

T = TypeVar('T')


ItemsInSchemaBase: Any = pydantic_model_creator(Items, name='ItemsIn', exclude=('id',))
ItemsSchemaBase: Any = pydantic_model_creator(Items, name='Items')
VotesSchemaBase: Any = pydantic_model_creator(Votes, name='Votes')
VotesInSchemaBase: Any = pydantic_model_creator(Votes, name='VotesIn', exclude=('id',))


class ItemsInSchema(ItemsInSchemaBase):
    pass


class ItemsSchema(ItemsSchemaBase):
    pass


class VotesSchema(VotesSchemaBase):
    item_id: int


class VotesInSchema(VotesInSchemaBase):
    item_id: int


class SettingsInSchema(PydanticModel, GenericModel, Generic[T]):
    name: str
    value: T

    class Config:
        orig_model = Settings


class SettingsSchema(SettingsInSchema, GenericModel, Generic[T]):
    type: str


class ItemsVotesSchema(PydanticModel):
    id: int
    name: str
    votes_count: int
