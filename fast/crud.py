from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserCreateWithIds

# def get_user(db: Session, skip: int= 0, limit: int = 5):
#     return db.query(User).offset(skip).limit(limit).all()

# def get_user_by_id(db: Session, user_id: int):
#     return db.query(User).filter(User.user_id == user_id).first()

def create_user(db:Session, user_create: UserCreate):
    db_user = User(**user_create.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# def create_user_with_ids(db: Session, user_create: UserCreateWithIds):
#     db_user = User(**user_create.dict())
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def remove_user(db:Session, user_id: int):
#     db_user = get_user_by_id(db=db,user_id=user_id)
#     db.delete(db_user)
#     db.commit()

# def update_user(db: Session, user_id: int, email: str, libary_id: str,phone_number: str):
#     db_user = get_user_by_id(db_user = get_user_by_id(db=db,user_id=user_id))
#     db_user.library_id = libary_id
#     db_user.phone_number = phone_number
#     db.commit()
#     db.refresh(db_user)
#     return db_user
