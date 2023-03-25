from fastapi import APIRouter, Depends
from sqlalchemy import select
from database import AsyncSession, get_async_session
from post.models import post_table
from typing import Mapping, List,Optional
from post.schemas import Post

post_router = APIRouter(prefix="/v1/posts", tags=["Записи (Посты)"])

@post_router.get("/",response_model=List[Post])
async def get_posts(session: AsyncSession = Depends(get_async_session)):
    query = select(post_table).order_by(post_table.c.id)
    result = await session.execute(query)
    resp = result.all()
    return resp

@post_router.get("/{post_id}",response_model=Post)
async def get_specific_post(
    post_id: int, session: AsyncSession = Depends(get_async_session)
    ):
    query = select(post_table).where(post_table.c.id == post_id)
    result = await session.execute(query)
    resp = result.first()
    return resp

async def post_by_slug(slug:str,  session: AsyncSession = Depends(get_async_session)):
    query = select(post_table).where(post_table.c.slug == slug)
    result = await session.execute(query)
    resp = result.first()
    return resp


@post_router.get("/{slug}",response_model=Post)
async def get_specific_post_by_slug(post:Post = Depends(post_by_slug)):
    return post