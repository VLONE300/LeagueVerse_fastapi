from . import models, schemas
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/leagues/', response_model=List[schemas.League])
async def get_leagues(db: Session = Depends(get_db)):
    leagues = db.query(models.League).all()
    return leagues
