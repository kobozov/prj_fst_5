from datetime import datetime
from pydantic import BaseModel


class BlogCreate(BaseModel):
    id: int
    title: str
    slug: str
    content: str
    create_at: datetime
    type: str
