from fastapi import FastAPI
from post.router import post_router

app=FastAPI(title="Kobozov blog")


app.include_router(post_router)

