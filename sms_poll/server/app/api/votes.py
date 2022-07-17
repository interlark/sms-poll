from fastapi import APIRouter, Depends, status

from ..config import config
from ..models import Votes
from ..schemas import VotesInSchema, VotesSchema
from .dependencies import verify_localhost

router = APIRouter(prefix='/votes')


if config.debug:
    @router.post('/', response_model=VotesSchema, status_code=status.HTTP_201_CREATED)
    async def add(sms: VotesInSchema, dependency=Depends(verify_localhost)):
        """Add vote for an item."""
        return await Votes.create(**sms.dict(exclude_unset=True))


@router.delete('/', status_code=status.HTTP_202_ACCEPTED)
async def clear(dependency=Depends(verify_localhost)):
    """Clear all votes."""
    await Votes.all().delete()
