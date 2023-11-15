from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from schemas import CreateMusicLibraryRequest
from sqlalchemy.orm import Session
from database import get_db
from models import Music_Library, Song, Music_Generator, User, Streaming_Service

app = FastAPI()

# app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"])  # only allow requests from React site


@app.post("/")
def create(details: CreateMusicLibraryRequest, db: Session = Depends(get_db)):
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
def home():
    return {"response": "hello"}
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

#sample login func for api connection testing
@app.post("/login")
def process_login(username: str, password: str):
    if username == password:
        return {"response": "true"}
    return {"response": "false"}