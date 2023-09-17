# import libraries
from sqlalchemy.orm import Session

# db models and pydantic models
from ..models import users, users_db


# USER CRUD OPERATIONS
def get_all_users(db: Session):
    return db.query(users_db.User).all()