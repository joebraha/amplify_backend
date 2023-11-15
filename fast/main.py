from fastapi import FastAPI, Depends
from .schemas import CreateMusicLibraryRequest
from sqlalchemy.orm import Session
from .database import get_db
from .models import Music_Library, Song, Music_Generator, User, Streaming_Service

app = FastAPI()

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