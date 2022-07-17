from fastapi import APIRouter, HTTPException, Request
from starlette.responses import RedirectResponse

from .dependencies import verify_localhost

router = APIRouter(prefix='')


@router.get('/')
async def index_redirect(request: Request):
    """Redirect localhost to admin page, others to poll page."""
    try:
        await verify_localhost(request)
        return RedirectResponse(url='admin')
    except HTTPException:
        return RedirectResponse(url='poll')
