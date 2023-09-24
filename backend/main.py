from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User

import os

DATABASE_URL = os.getenv('DATABASE_URL')


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

@app.get("/")
async def read_root():
    session = SessionLocal()
    users = session.query(User).all()
    session.close()
    return {"users": [user.name for user in users]}
