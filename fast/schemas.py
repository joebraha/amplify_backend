from pydantic import BaseModel

class CreateMusicLibraryRequest(BaseModel):

    songs: str
    storage_used: int
    user_id: int
    storage_left: int

class CreateUserRequest(BaseModel):

    user_id: int
    email: str
    library_id: int
    phone_number: str

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
