from pydantic import BaseModel, Field, ValidationError


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
