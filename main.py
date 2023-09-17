# import libraries
from fastapi import FastAPI
from functools import lru_cache

# import config file
from . import config
#import db models
from .models import users_db
# import db utils
from .database.db import SessionLocal, engine

# create tables
users_db.Base.metadata.create_all(bind=engine)


# fastapi app
app = FastAPI()

# Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# environment variables
@lru_cache()
def get_settings():
    return config.Settings()

# root route to check server status
@app.get("/")
async def root():
    return {"message": "Server is running"}