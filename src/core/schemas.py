from pydantic import BaseModel


class LeagueBase(BaseModel):
    name: str
    logo_path: str


class LeagueCreate(LeagueBase):
    pass


class League(LeagueBase):
    id: int

    class Config:
        orm_mode = True
