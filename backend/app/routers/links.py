from fastapi import APIRouter, Request, status

from app import storage
from app.schemas import LinkCreate, LinkResponse

router = APIRouter(prefix="/api/links", tags=["Links"])

@router.post("", response_model=LinkResponse, status_code=status.HTTP_201_CREATED)
def create_link(dados: LinkCreate, request: Request):
    url = str(dados.url)
    code = storage.save_url(url)
    return LinkResponse(
        code=code,
        url=url,
        short_url=f"{request.base_url}{code}"
    )