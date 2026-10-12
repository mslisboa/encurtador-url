from pydantic import BaseModel, HttpUrl

class LinkCreate(BaseModel):
    url: HttpUrl

class LinkResponse(BaseModel):
    code: str
    url: str
    short_url: str