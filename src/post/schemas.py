from datetime import datetime
from pydantic import BaseModel

class MyBaseModel(BaseModel):
    class Config:
        orm_mode = True

class PostCreate(MyBaseModel):
    id: int
    title: str
    slug: str
    content: str
    create_at: datetime
    type: str

class Post(MyBaseModel):
    id: int
    title: str
    slug: str
    content: str
    create_at: datetime

