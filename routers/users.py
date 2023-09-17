# import libraries
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# import database local sesssion
from ..main import get_db
# import crud functions
from ..database.crud import get_all_users
# import db models and pydantic models
from ..models import users

# user routes are prefixed with '/users'
router = APIRouter(
    prefix="/users",
)

# GET routes
@router.get("/", response_model=list[users.User])
async def all_users(database_session: Session = Depends(get_db)):
    list_of_all_users = get_all_users(db=database_session)
    return list_of_all_users


# POST routes

# PUT routes

# DELETE routes