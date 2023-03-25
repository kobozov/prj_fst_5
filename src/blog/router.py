from fastapi import APIRouter, Depends
from sqlalchemy import select
from database import AsyncSession, get_async_session
from blog.models import blog_table


blog_router = APIRouter(
    prefix="/blog",
    tags=["Блог"]
)


@blog_router.get("/{blog_id}")
async def get_specific_blog(blog_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(blog_table).where(blog_table.c.id == blog_id)
    result = await session.execute(query)
    return result.all()