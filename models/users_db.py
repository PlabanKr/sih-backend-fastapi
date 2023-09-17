import enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Enum
from sqlalchemy.orm import relationship

# import base class for the database models
from ..database.db import Base

# Types and Enums
class SpecializationEnum(enum.Enum):
    medical = 'medical'
    search_and_rescue = 'search-and-rescue'
    fire_fighter = 'fire-fighter'
    water_rescue = 'water-rescue'
    animal_rescue = 'animal-rescue'
    helicopter_rescue = 'helicopter-rescue'

# Database models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    middle_name = Column(String)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    dob = Column(Date)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    user_image = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)

class Rescuers(Base):
    __tablename__ = "rescuers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    middle_name = Column(String)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    dob = Column(Date)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    rescuer_image = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    specialization = Column(Enum(SpecializationEnum))
    availability_status = Column(Boolean, nullable=False)
