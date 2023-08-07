from typing import Union

from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from models.schemas import User as DBUser
router = APIRouter()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None
    balance: float = 0.0


class User(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None]
    balance: float


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: Union[str, None] = None
    balance: float = 0.0


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
#     print("User saved! ..not really")
#     return user_in_db
#
#
# @router.post("/user/", response_model=User)
# async def create_user(user_in: UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved

def convert_db_user_to_model(user: DBUser):
    return User(email=user.email, username=user.username, fullname=user.fullname, balance=user.balance)