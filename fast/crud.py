from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate

def create_user(db:Session, user_create: UserCreate):
    db_user = User(**user_create.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
