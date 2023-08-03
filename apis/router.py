from fastapi import APIRouter

import users

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])

