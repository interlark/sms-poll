from fastapi import HTTPException, Request, Response
from starlette.middleware.base import (BaseHTTPMiddleware,
                                       RequestResponseEndpoint)

from .api.dependencies import verify_localhost


class LocalAdminMiddleware(BaseHTTPMiddleware):
    """Middleware for "/admin" zone protection from external access."""
    async def dispatch(self, request: Request,
                       call_next: RequestResponseEndpoint) -> Response:
        if request.scope['path'].startswith('/admin'):
            try:
                await verify_localhost(request)
            except HTTPException as e:
                return Response(content=e.detail, status_code=e.status_code)

        response = await call_next(request)
        return response
