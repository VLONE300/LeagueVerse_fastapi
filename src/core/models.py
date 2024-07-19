from sqlalchemy import Column, Integer, String

from src.database import Base


class League(Base):
    __tablename__ = 'leagues'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    logo_path = Column(String, nullable=True)


class Team(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    conference = Column(String, nullable=True)
    division = Column(String, nullable=True)


class Standings(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    wins = Column(Integer, default=0)
    losses = Column(Integer, default=0)
