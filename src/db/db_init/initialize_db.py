from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    firstname = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(100), nullable=False)
    password_hashed = Column(String(200), nullable=False)
    profile_b64 = Column(String(), nullable=True)
    #time_created = Column(String(10), nullable=False)

    apartments = relationship("Apartments", back_populates="users")


class Apartments(Base):
    __tablename__ = "apartments"
    
    apartment_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    
    # Relationship to the user who owns this apartment
    user = relationship("Users", back_populates='apartments')

    # One-to-Many: One apartment can have many photos
    photos = relationship("Photos", back_populates="apartments")

    # One-to-Many: One apartment can have many residents
    residents = relationship("Residents", back_populates="apartments")


class Photos(Base):
    __tablename__ = "photos"

    photo_id = Column(Integer, primary_key=True)
    apartment_id = Column(Integer, ForeignKey("apartments.apartment_id"), nullable=False)
    photo_b64 = Column(String(),nullable=False)

    apartments = relationship("Apartments", back_populates="photos")

class Residents(Base):
    __tablename__ = "residents"

    resident_id = Column(Integer, primary_key=True)
    apartment_id = Column(Integer, ForeignKey("apartments.apartment_id"), nullable=False)
    firstname = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(100), nullable=False)
    profile_b64 = Column(String(), nullable=True)
    
    apartments = relationship("Apartments", back_populates="residents")