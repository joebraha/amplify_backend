from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, UniqueConstraint

from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func 

import datetime as _dt
import passlib.hash as _hash


# class Music_Generator(Base):
#     __tablename__ = "music_generator"
    
#     key_words = Column(String, primary_key = True)
#     user_id = Column(Integer, ForeignKey('songs.user_id'),primary_key = True)
#     genres = Column(String)
#     streaming_service_info = Column(String)

class User(Base):
    __tablename__ = "user"

    username = Column(String, primary_key = True, index = True) 
    password = Column(String)
    email = Column(String)
    phone_number = Column(String)
    user_id = Column(Integer, index=True, autoincrement=True, unique=True, primary_key=True)

    __table_args__ = (UniqueConstraint('username', 'password'),)

class Song(Base):
    __tablename__ = "songs"

    song_file = Column(String, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    song_id = Column(Integer, autoincrement = True, unique = True, primary_key=True)

    
# class Streaming_Service(Base):
#     __tablename__ = "streaming_service"

#     user_id = Column(Integer, ForeignKey('user.user_id'), primary_key = True)
#     email = Column(String)
#     service_songs = Column(String)
#     service_password = Column(String) 
#     service_username = Column(String)
#     service_name = Column(String,primary_key = True)

# class Music_Library(Base):
#     __tablename__ = "music_library"

#     song = Column(String)
#     user_id = Column(Integer,ForeignKey('user.user_id'), primary_key = True,)
