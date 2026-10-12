from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse

from app import storage

router = APIRouter(tags=["redirect"])

@router.get("/{code}")
def redirect_to_url(code: str):
    url = storage.get_url(code)
    if url is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Link not found")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
