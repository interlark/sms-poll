from typing import List

from fastapi import APIRouter, Depends, Response, status
from tortoise.functions import Count
from tortoise.transactions import in_transaction

from ..models import Items, Settings
from ..schemas import (ItemsInSchema, ItemsSchema, ItemsVotesSchema,
                       SettingsSchema)
from .dependencies import verify_localhost

router = APIRouter(prefix='/items')


@router.get('/', response_model=List[ItemsVotesSchema])
async def get():
    """Get all items with associated number of votes."""
    distinct_poll_obj = await Settings.all().filter(name='distinct_poll').get()
    distinct_poll = await SettingsSchema[bool].from_tortoise_orm(distinct_poll_obj)

    result = (await Items.all()
              .annotate(votes_count=Count('votes__phone', distinct=distinct_poll.value))
              .group_by('name')
              .order_by('id')
              .values('id', 'name', 'votes_count'))
    return result


@router.post('/', response_model=ItemsSchema, status_code=status.HTTP_201_CREATED)
async def add(participant: ItemsInSchema, dependency=Depends(verify_localhost)):
    """Add item."""
    async with in_transaction():
        last_participant = await Items.all().order_by('-id').first()
        next_id = 1 if last_participant is None else last_participant.id + 1

        participant_dict = participant.dict(exclude_unset=True)
        participant_dict['id'] = next_id

        return await Items.create(**participant_dict)


@router.put('/{item_id}', response_model=ItemsSchema, status_code=status.HTTP_202_ACCEPTED)
async def edit(item_id: int, participant: ItemsInSchema, dependency=Depends(verify_localhost)):
    """Edit item with specific ID."""
    instance = await Items.filter(id=item_id).get()
    return await instance.update_from_dict(participant.dict(exclude_unset=True)).save()


@router.delete('/{item_id}', status_code=status.HTTP_202_ACCEPTED)
async def remove(item_id: int, dependency=Depends(verify_localhost)):
    """Delete a participant with specific ID."""
    deleted_count = await Items.filter(id=item_id).delete()
    if not deleted_count:
        return Response(f'Participant with id={item_id} not found',
                        status_code=status.HTTP_404_NOT_FOUND)


@router.delete('/', status_code=status.HTTP_202_ACCEPTED)
async def clear(dependency=Depends(verify_localhost)):
    """Clear all participants."""
    await Items.all().delete()
