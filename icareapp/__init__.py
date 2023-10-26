import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from .database import SessionLocal
from instance.config import SECRET_KEY, DATABASE_URI


starter = FastAPI(title="iCare HMS", description="A system that helps manage the information related to health care and aids in the job completion of health care")


engine = create_engine(DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: DeclarativeMeta = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




from icareapp import routes


starter.include_router(routes.care_router, dependencies=[Depends(get_db)])


