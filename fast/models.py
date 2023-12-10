from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from database import Base


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
