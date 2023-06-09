from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData


metadata = MetaData()

post_table = Table(
    "post",
    metadata,
    Column("id", Integer, primary_key=True,autoincrement=True),
    Column("title", String),
    Column("slug", String),
    Column("content", String),
    Column("create_at", TIMESTAMP),
)

class Post(object):
    pass

