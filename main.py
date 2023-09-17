# import libraries
from fastapi import FastAPI
from functools import lru_cache

# import config file
from . import config

# fastapi app
app = FastAPI()

# environment variables
@lru_cache()
def get_settings():
    return config.Settings()

# root route to check server status
@app.get("/")
async def root():
    return {"message": "Server is running"}