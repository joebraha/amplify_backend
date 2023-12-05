from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func 

import datetime as _dt
import passlib.hash as _hash

class Song(Base):
    __tablename__ = "songs"

    song_name = Column(String, primary_key = True)
    length = Column(String)
    user_id = Column(Integer, ForeignKey('user.user_id'), primary_key = True)
    genre = Column(String)


class Music_Generator(Base):
    __tablename__ = "music_generator"
    
    key_words = Column(String, primary_key = True)
    user_id = Column(Integer, ForeignKey('songs.user_id'),primary_key = True)
    genres = Column(String)
    streaming_service_info = Column(String)

class User(Base):
    __tablename__ = "user"

    username = Column(String, primary_key = True, index = True) 
    password = Column(String, primary_key = True, index = True)
    user_id = Column(Integer, primary_key = True, index = True, autoincrement=True)
    email = Column(String, unique = True, index = True)
    library_id = Column(Integer, ForeignKey('Music_Library.user_id'))
    phone_number = Column(String)

    # hashed_password = Column(String)

    # leads = relationship("Lead", back_populates="owner")

    # def verify_password(self, password: str):
    #     return _hash.bcrypt.verify(password, self.hashed_password)

class Streaming_Service(Base):
    __tablename__ = "streaming_service"

    user_id = Column(Integer, ForeignKey('user.user_id'), primary_key = True)
    email = Column(String)
    service_songs = Column(String)
    service_password = Column(String) 
    service_username = Column(String)
    service_name = Column(String,primary_key = True)

class Music_Library(Base):
    __tablename__ = "Music_Library"

    songs = Column(String)
    storage_used = Column(Integer)
    user_id = Column(Integer,ForeignKey('user.user_id'), primary_key = True,)
    storage_left = Column(Integer)

class Lead(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("user.user_id"))
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    company = Column(String, index=True, default="")
    note = Column(String, default="")
    date_created = Column(DateTime, default=_dt.datetime.utcnow)
    date_last_updated = Column(DateTime, default=_dt.datetime.utcnow)

    owner = relationship("User", back_populates="leads")