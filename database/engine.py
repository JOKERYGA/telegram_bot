import os
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from database.models import Base
from database.orm_query import orm_add_banner_description, orm_create_categories

from common.text_for_db import categories, description_for_info_pages

# DB_LITE=sqlite+aiosqlite:///my_base.db
# DB_URL=postgresql+asyncpg://login:password@localhost:5432/db_name
# engine = create_async_engine(os.getenv('DB_lite'), echo=True)


# echo=True - все sql запросы будут выводиться в терминал(отладка)
engine = create_async_engine(os.getenv('DB_URL'), echo=True)

# будет брать сессии чтобы делать запросы в нашу баззу данных
# expire_on_commit=False - чтоб мы могли воспользоваться нашей сессией повторно после коммита
# async_session - создает фабрику сессий, bind=engine указывает, что сессии будут привязаны к асинхронному движку, созданному ранее.
session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with session_maker() as session:
        await orm_create_categories(session, categories)
        await orm_add_banner_description(session, description_for_info_pages)

async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)