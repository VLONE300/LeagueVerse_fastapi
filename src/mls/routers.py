from typing import List
from . import models, schemas
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


@router.get('/teams/', response_model=List[schemas.MLSTeam])
async def get_mls_teams(db: Session = Depends(get_db)):
    mls_teams = db.query(models.MLSTeam).all()
    return mls_teams
