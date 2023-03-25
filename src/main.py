from fastapi import FastAPI
from blog.router import blog_router

app=FastAPI(title="Kobozov blog")


app.include_router(blog_router)

