from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
#tutaj 2 czesc
from sqlalchemy.orm import sessionmaker


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

    apartments = relationship("Apartments", back_populates="user")


class Apartments(Base):
    __tablename__ = "apartments"
    
    apartment_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    
    # Relationship to the user who owns this apartment
    user = relationship("Users", back_populates='apartments')

    # One-to-Many: One apartment can have many photos
    photos = relationship("Photos", back_populates="apartment")

    # One-to-Many: One apartment can have many residents
    residents = relationship("Residents", back_populates="apartment")

    info = relationship("Info", back_populates="apartment")

class Info(Base):
    __tablename__ = "info"
    
    apartment_id = Column(Integer, ForeignKey("apartments.apartment_id"), primary_key=True)
    miasto = Column(String(50), nullable=False)
    ulica = Column(String(50), nullable=False)
    adres_pocztowy = Column(String(50), nullable=False)
    numer_budynku = Column(Integer, nullable=False)
    numer_lokalu = Column(Integer, nullable=True)
    metraz = Column(Integer, nullable=False)
    pokoje = Column(Integer, nullable=False)
    wlasciciel = Column(String(100), nullable = False)
    stan = Column(String(50), nullable = True)
    wc_osobno = Column(Boolean, nullable=False)
    cena_wynajmu = Column(Integer, nullable=False)

    apartment = relationship("Apartments", back_populates="info")



class Photos(Base):
    __tablename__ = "photos"

    photo_id = Column(Integer, primary_key=True)
    apartment_id = Column(Integer, ForeignKey("apartments.apartment_id"), nullable=False)
    photo_b64 = Column(String(),nullable=False)

    apartment = relationship("Apartments", back_populates="photos")

class Residents(Base):
    __tablename__ = "residents"

    resident_id = Column(Integer, primary_key=True)
    apartment_id = Column(Integer, ForeignKey("apartments.apartment_id"), nullable=False)
    firstname = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(100), nullable=False)
    profile_b64 = Column(String(), nullable=True)
    miasto = Column(String(50), nullable=False)
    ulica = Column(String(100), nullable=False)
    adres_pocztowy = Column(String(50), nullable=False)
    numer_budynku = Column(Integer, nullable=False)
    numer_lokalu = Column(Integer, nullable=True)

    
    apartment = relationship("Apartments", back_populates="residents")

engine = create_engine("sqlite:///db.db")
Base.metadata.create_all(engine)


#tutaj 2 czesc

class UserData:
    def __init__(self, username, firstname, surname, email, phone, password_hashed, profile_b64=None):
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.email = email
        self.phone = phone
        self.password_hashed = password_hashed
        self.profile_b64 = profile_b64


Session = sessionmaker(bind=engine)
db_session = Session()






