from datetime import timedelta, datetime
from fastapi import APIRouter, Request, status, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from icareapp import starter, models, schemas
from icareapp.dependencies import get_db
from fastapi.security import OAuth2PasswordRequestForm


care_router = APIRouter()


#     --   G E T   R E Q U E S T S   --

@starter.get("/")
async def get_index():
    return {"message": "Welcome to iCare HMS"}





#     --   C R E A T E   R E Q U E S T S   --





#     --   U P D A T E   R E Q U E S T S   --





#     --   D E L E T E   R E Q U E S T S   --