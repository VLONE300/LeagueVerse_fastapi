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


@router.get('/teams/', response_model=List[schemas.NBATeam])
async def get_nba_teams(db: Session = Depends(get_db)):
    nba_teams = db.query(models.NBATeam).all()
    return nba_teams
