from fastapi import HTTPException, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from .api.dependencies import verify_localhost


class LocalAdminMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.scope['path'].startswith('/admin'):
            try:
                await verify_localhost(request)
            except HTTPException as e:
                return Response(content=e.detail, status_code=e.status_code)
        
        response = await call_next(request)
        return response
