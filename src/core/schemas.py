from typing import Optional
from pydantic import BaseModel


class LeagueBase(BaseModel):
    name: str
    logo_path: Optional[str]


class League(LeagueBase):
    id: int

    class Config:
        from_attributes = True
