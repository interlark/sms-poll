from fastapi import HTTPException, Request


async def verify_localhost(request: Request):
    if request.client.host not in ('127.0.0.1', 'localhost'):
        raise HTTPException(status_code=401, detail='Only localhost allowed!')
