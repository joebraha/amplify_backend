from fastapi import FastAPI, Depends, Response
from schemas import UserCreate
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine
import crud
from models import Song, User
from fastapi.exceptions import HTTPException
import requests
from schemas import ValidationError

from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

AI_source = "https://9b9d-146-148-64-104.ngrok.io"
AI_URL = AI_source + "/run/"


origins = [
    "*",  # Add the actual origin of your frontend application
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

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/CreateAccount/")
async def create_user(request: UserCreate,db: Session = Depends(get_db)):
    try:
        print("Received request:", request.dict())
        crud.create_user(db, request)
    except ValidationError as e:
        print("Validation Error:", e.json())
        raise HTTPException(status_code=422, detail="Validation Error")
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/get_user/{username}")
def get_user(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/delete_user/{username}")
def delete_user(username: str, db: Session = Depends(get_db)):
    # Query the database to find the user by username
    user = db.query(User).filter(User.username == username).first()

    # If user not found, raise an HTTPException with a 404 status code
    if user is None:
        raise HTTPException(status_code=404, detail=f"User with username {username} not found")

    # Remove the user from the database
    db.delete(user)
    db.commit()

    return {"message": f"User with username {username} deleted successfully"}

@app.post("/CreateSong/{user_id}")
async def upload_song(user_id: int, file: str, db: Session = Depends(get_db)):
    # Check if the user exists
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    # Save the song to the database
    song = Song(song_file=file, user_id=user_id)
    db.add(song)
    db.commit()

    return {"filename": file}

@app.get("/UserSongs/{user_id}")
async def get_user_songs(user_id: int, db: Session = Depends(get_db)):
    try:
        result = db.query(Song).filter(Song.user_id == user_id).order_by(Song.song_id.desc()).limit(4).all()
        return result
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/UserFeed/{user_id}")
async def get_user_songs(user_id: int, db: Session = Depends(get_db)):
    try:
        result = db.query(Song).filter(Song.user_id != user_id).order_by(Song.song_id.desc()).limit(4).all()
        return result
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.delete("/Song/{song_file}")
async def get_songs_by_id(song_file: str, db: Session = Depends(get_db)):
    try:
        result = db.query(Song).filter(Song.song_file == song_file).first()
        return result
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/Song/{song_file}")
async def get_songs_by_id(song_file: str, db: Session = Depends(get_db)):
    try:
        song = db.query(Song).filter(Song.song_file == song_file).first()
        if song is None:
            raise HTTPException(status_code=404, detail=f"Song with file_name {song} not found")
        db.delete(song)
        db.commit()
        return {"message": f"User with username {song} deleted successfully"}
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

# prompts AI server for wav file. Returns file (not JSON)
@app.get("/generate/{input}", response_class=Response)
async def prompt_model(input: str):
    r = requests.get(AI_URL + input)
    print(r)
    if r.status_code == 404:
        raise HTTPException(status_code=404, detail="AI Server Error") 
    return Response(content=r.content, status_code=200)
