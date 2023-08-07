from sqlalchemy.orm import Session
from models.user import *
import models.schemas as schemas
from models.user import convert_db_user_to_model
from fastapi import APIRouter, Body, Depends
from apis import deps

router = APIRouter()


@router.get('/get-user')
def get_user(user_id: int, db: Session = Depends(deps.get_db)) -> dict:
    user = db.query(schemas.User).filter(schemas.User.id == user_id).first()
    print(convert_db_user_to_model(user))
    return {"header": "asdjkalsd"}


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.User):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
