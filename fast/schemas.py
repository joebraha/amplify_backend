from pydantic import BaseModel, Field
from typing import Optional
import datetime as _dt

class UserBase(BaseModel):
    email: str
    library_id: int
    

class UserCreate(UserBase):
    hased_password: str

    class config: 
        orm_mode = True

class leadBase(BaseModel):
    name: str
    email: str
    
class leadCreate(leadBase):
    pass

class lead(leadBase):
    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime # needed? 

    class config:
        orm_mode = True


class User(BaseModel):
    user_id: Optional[int] = None
    email: Optional[str] = None
    library_id: Optional[int] = None
    phone_number: Optional[str] = None

    class Config:
        orm_mode = True

class RequestUser(BaseModel):
    parameter: User = Field(...)


class CreateMusicLibraryRequest(BaseModel):

    songs: str
    storage_used: int
    user_id: int
    storage_left: int


class CreateSongRequest(BaseModel):

    song_name: str
    length: str
    user_id: int
    genre: str

class CreateStreamingServiceRequest(BaseModel): 

    user_id: int
    email: str
    service_songs: str
    service_password: str
    service_username: str 
    service_name: str

class CreateMusicGeneratorRequest(BaseModel): 
    key_words: str
    user_id: int
    genres: str
    streaming_service_info: str
