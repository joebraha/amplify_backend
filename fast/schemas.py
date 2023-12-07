from pydantic import BaseModel, Field
from typing import Optional
import datetime as _dt

# class UserBase(BaseModel):
#     email: str
#     library_id: int
    

class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    phone_number: str

    
class UserCreateWithIds(UserCreate):
    user_id: int

    class Config:
        orm_mode = True

class SongCreate(BaseModel):
    song_file: str
    
class SongCreateWithIds(SongCreate):
    user_id: int
    song_id: int

    class Config:
        orm_mode = True

# class RequestUser(BaseModel):
#     parameter: UserCreate = Field(...)


# class CreateMusicLibraryRequest(BaseModel):

#     songs: str
#     storage_used: int
#     user_id: int
#     storage_left: int


# class CreateSongRequest(BaseModel):

#     song_name: str
#     length: str
#     user_id: int
#     genre: str

# class CreateStreamingServiceRequest(BaseModel): 

#     user_id: int
#     email: str
#     service_songs: str
#     service_password: str
#     service_username: str 
#     service_name: str

# class CreateMusicGeneratorRequest(BaseModel): 
#     key_words: str
#     user_id: int
#     genres: str
#     streaming_service_info: str
