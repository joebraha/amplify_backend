from fastapi import FastAPI, Depends
from schemas import CreateMusicLibraryRequest, User, RequestUser
from sqlalchemy.orm import Session
import models
from database import SessionLocal,engine  # Adjust the import path accordingly
from typing import Annotated
import crud
from models import Music_Library, Song, Music_Generator, User, Streaming_Service
from fastapi.exceptions import HTTPException
import requests

from typing import List
import fastapi.security as _security 
from fastapi.middleware.cors import CORSMiddleware

import sqlalchemy.orm as _orm

import services as _services, schemas as _schemas
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

AI_URL = "https://ba05-34-123-11-187.ngrok.io/run/"



origins = [
    "http://localhost:3000/",  # Add the actual origin of your frontend application
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/CreateAccount")
async def create_user(request: RequestUser,db: Session = Depends(get_db)):
    crud.create_user(db, request.parameter)
    return {"message": "Created new user"}

@app.post("/")
def create_music_library(details: CreateMusicLibraryRequest, db: Session = Depends(get_db)):
    to_create = Music_Library(
        songs = details.songs,
        storage_used = details.storage_used,
        user_id = details.user_id,
        storage_left = details.storage_left,
    )
    db.add(to_create)
    db.commit()
    return{
        "success": True,
        "create_id": to_create.id
    }

@app.get("/")
def get_by_id(user_id: int, db: Session = Depends(get_db)):
    return db.query(Music_Library).filter(Music_Library.user_id == user_id).first()

@app.delete("/")
def delete(user_id: int, db: Session = Depends(get_db)):
    db.query(Music_Library).filter(Music_Library.user_id == user_id).delete()
    db.commit()
    return {"success": True}

@app.put("/")
def update_item(user_id: int, db: Session = Depends(get_db)):
    return {'name':item.name, } 

@app.get("/")
async def post_recent_music(recent_songs: str, db: Session = Depends(get_db)):
    result = db.query(Song.song_name).order_by(Song.song_id.desc()).limit(5)
    return result

@app.get("/account/playlists")
async def post_user_playlists(user_id: int, db: Session = Depends(get_db)):
    result = db.query(Song.song_name).filter(Song.user_id == user_id).order_by(Song.song_id.desc()).limit(5)
    return result

# prompts AI server for wav file. Returns file (not JSON)
@app.get("/generate/{input}")
async def prompt_model(input: str):
    r = await requests.get(AI_URL + input)
    return r

@app.post("/api/users")
async def create_user(
    user: _schemas.UserCreate, db: _orm.Session = Depends(_services.get_db)
):
    db_user = await _services.get_user_by_email(user.email, db)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already in use")

    user = await _services.create_user(user, db)

    return await _services.create_token(user)

@app.post("/api/token")
async def generate_token(
    form_data: _security.OAuth2PasswordRequestForm = Depends(),
    db: _orm.Session = Depends(_services.get_db),
):
    user = await _services.authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    return await _services.create_token(user)


@app.get("/api/users/me", response_model=_schemas.User)
async def get_user(user: _schemas.User = Depends(_services.get_current_user)):
    return user


@app.get("/api")
async def root():
    return {"message": "Awesome Leads Manager"}