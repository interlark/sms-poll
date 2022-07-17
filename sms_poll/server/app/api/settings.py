from typing import List

from fastapi import APIRouter, Depends, Response, status
from tortoise.exceptions import FieldError

from ..models import Settings
from ..schemas import SettingsInSchema, SettingsSchema
from .dependencies import verify_localhost

router = APIRouter(prefix='/settings')


@router.get('/flags', response_model=List[SettingsSchema[bool]])
async def get_flags():
    """Get all settins flags."""
    try:
        return await Settings.all().filter(type='FLAG')
    except FieldError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.get('/flags/{name}', response_model=SettingsSchema[bool])
async def get_flag(name: str):
    """Get settings flag."""
    try:
        return await Settings.all().filter(name=name, type='FLAG').get()
    except FieldError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.put('/flags', response_model=SettingsSchema[bool], status_code=status.HTTP_202_ACCEPTED)
async def set_flag(data: SettingsInSchema[bool], dependency=Depends(verify_localhost)):
    """Set settings flag."""
    flag = await Settings.all().filter(name=data.name, type='FLAG').get()
    flag.update_from_dict(data.dict(exclude_unset=True))
    await flag.save()
    return flag


@router.get('/strings', response_model=List[SettingsSchema[str]])
async def get_strings():
    """Get all strings."""
    return await Settings.all().filter(type='STRING')


@router.get('/strings/{name}', response_model=SettingsSchema[str])
async def get(name: str):
    """Get a string."""
    return await Settings.filter(name=name, type='STRING').get()


@router.put('/strings', response_model=SettingsSchema[str], status_code=status.HTTP_202_ACCEPTED)
async def edit(string: SettingsInSchema[str], dependency=Depends(verify_localhost)):
    """Edit string."""
    string_obj = await Settings.filter(name=string.name, type='STRING').get()
    string_obj.update_from_dict(string.dict(exclude_unset=True))
    await string_obj.save()
    return string_obj
