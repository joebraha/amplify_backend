from fastapi import FastAPI, Depends
from .schemas import CreateMusicLibraryRequest
from sqlalchemy.orm import Session
from .database import get_db
from .models import Music_Library, Song, Music_Generator, User, Streaming_Service

from typing import List
import fastapi as _fastapi
import fastapi.security as _security

import sqlalchemy.orm as _orm

import services as _services, schemas as _schemas

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


@app.get("/")
async def post_recent_music(recent_songs: str, db: Session = Depends(get_db)):
    result = db.query(Song.song_name).order_by(Song.song_id.desc()).limit(5)
    return result

@app.get("/account/playlists")
async def post_user_playlists(user_id: int, db: Session = Depends(get_db)):
    result = db.query(Song.song_name).filter(Song.user_id == user_id).order_by(Song.song_id.desc()).limit(5)
    return result

#################################################################################


@app.post("/api/users")
async def create_user(
    user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_user = await _services.get_user_by_email(user.email, db)
    if db_user:
        raise _fastapi.HTTPException(status_code=400, detail="Email already in use")

    user = await _services.create_user(user, db)
    return await _services.create_token(user)


@app.post("/api/token")
async def generate_token(
    form_data: _security.OAuth2PasswordRequestForm = _fastapi.Depends(),
    db: _orm.Session = _fastapi.Depends(_services.get_db),):
    user = await _services.authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise _fastapi.HTTPException(status_code=401, detail="Invalid Credentials")

    return await _services.create_token(user)


@app.get("/api/users/me", response_model=_schemas.User)
async def get_user(user: _schemas.User = _fastapi.Depends(_services.get_current_user)):
    return user


@app.post("/api/leads", response_model=_schemas.Lead)
async def create_lead(
    lead: _schemas.LeadCreate,
    user: _schemas.User = _fastapi.Depends(_services.get_current_user),
    db: _orm.Session = _fastapi.Depends(_services.get_db),):
    return await _services.create_lead(user=user, db=db, lead=lead)


@app.get("/api/leads", response_model=List[_schemas.Lead])
async def get_leads(
    user: _schemas.User = _fastapi.Depends(_services.get_current_user),
    db: _orm.Session = _fastapi.Depends(_services.get_db),):
    return await _services.get_leads(user=user, db=db)


@app.get("/api/leads/{lead_id}", status_code=200)
async def get_lead(
    lead_id: int,
    user: _schemas.User = _fastapi.Depends(_services.get_current_user),
    db: _orm.Session = _fastapi.Depends(_services.get_db),):
    return await _services.get_lead(lead_id, user, db)


@app.delete("/api/leads/{lead_id}", status_code=204)
async def delete_lead(
    lead_id: int,
    user: _schemas.User = _fastapi.Depends(_services.get_current_user),
    db: _orm.Session = _fastapi.Depends(_services.get_db),):
    await _services.delete_lead(lead_id, user, db)
    return {"message", "Successfully Deleted"}


@app.put("/api/leads/{lead_id}", status_code=200)
async def update_lead(
    lead_id: int,
    lead: _schemas.LeadCreate,
    user: _schemas.User = _fastapi.Depends(_services.get_current_user),
    db: _orm.Session = _fastapi.Depends(_services.get_db),):
    await _services.update_lead(lead_id, lead, user, db)
    return {"message", "Successfully Updated"}


@app.get("/api")
async def root():
    return {"message": "Awesome Leads Manager"}