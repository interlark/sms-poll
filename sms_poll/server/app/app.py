from __future__ import annotations

from typing import Any
import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from tortoise.contrib.fastapi import register_tortoise

from .api.items import router as items_router
from .api.phone import router as phone_router
from .api.root import router as root_router
from .api.settings import router as settings_router
from .api.votes import router as votes_router
from .config import ROOT_DIR, config
from .middlewares import LocalAdminMiddleware
from .models import Settings, Votes
from .utils import PLATFORM

if PLATFORM == 'android':
    from .android import (get_phone_number, start_sms_reciever,
                          stop_sms_reciever)


def create_app() -> FastAPI:
    """Create app and DB."""
    app = FastAPI()

    app.include_router(phone_router)
    app.include_router(items_router)
    app.include_router(votes_router)
    app.include_router(settings_router)
    app.include_router(root_router)

    app.mount('/admin', StaticFiles(
        directory=ROOT_DIR / 'static' / 'admin', html=True), name='admin'
    )
    app.mount('/poll', StaticFiles(
        directory=ROOT_DIR / 'static' / 'poll', html=True), name='poll'
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
    app.add_middleware(LocalAdminMiddleware)

    register_tortoise(
        app,
        db_url=f'sqlite://{config.db_path}',
        modules={'models': ['app.models']},
        generate_schemas=True,
        add_exception_handlers=True,
    )

    @app.on_event('startup')
    async def default_settings() -> None:
        phone_number = '(123) 456-7890'
        if PLATFORM == 'android':
            # Try to read phone number from SIM card
            retrieved_number = get_phone_number()
            if retrieved_number:
                phone_number = retrieved_number

        defaults: list[dict[str, Any]] = [
            {'name': '#', 'value': '#', 'type': 'STRING'},
            {'name': 'Item', 'value': 'Item', 'type': 'STRING'},
            {'name': 'Votes', 'value': 'Votes', 'type': 'STRING'},
            {'name': 'Phone', 'value': phone_number, 'type': 'STRING'},
            {'name': 'distinct_poll', 'value': True, 'type': 'FLAG'},
            {'name': 'light_theme_poll', 'value': False, 'type': 'FLAG'},
        ]

        all_settings = await Settings.all()
        for default in defaults:
            if not any(default['name'] == x.name for x in all_settings):
                await Settings.create(name=default['name'],
                                      value=default['value'], type=default['type'])

    @app.on_event('startup')
    async def start_services() -> None:
        if PLATFORM == 'android':
            import re

            def add_vote(phone: str, message: str):
                item_id = re.sub(r'[^\d]', '', message)
                if item_id:
                    vote = Votes(phone=phone, item_id=item_id)
                    asyncio.run_coroutine_threadsafe(vote.save(), loop)

            loop = asyncio.get_event_loop()
            start_sms_reciever(callback=add_vote)

    @app.on_event('shutdown')
    def stop_services() -> None:
        if PLATFORM == 'android':
            stop_sms_reciever()

    return app
