from fastapi import FastAPI
from pydantic import BaseModel

from app.db import SessionLocal, NewsModel, Base, engine

Base.metadata.create_all(bind=engine)


app = FastAPI()


class NewsMessage(BaseModel):
    content: str


@app.get("/news")
async def get_news():
    session = SessionLocal()

    return [NewsMessage(content=x.content) for x in session.query(NewsModel).all()]


@app.post("/news")
async def post_news(message: NewsMessage):
    session = SessionLocal()

    model = NewsModel(content=message.content)

    session.add(model)
    session.commit()

    return {"ok": True}
