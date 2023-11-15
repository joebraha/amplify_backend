from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func 

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

    user_id = Column(Integer, primary_key = True) 
    email = Column(String)
    library_id = Column(Integer, ForeignKey('Music_Library.user_id'))
    phone_number = Column(String)

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