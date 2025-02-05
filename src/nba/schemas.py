from typing import Optional
from pydantic import BaseModel


class NBATeamBase(BaseModel):
    name: str
    conference: Optional[str]
    division: Optional[str]
    team_logo: Optional[str]

    class Config:
        from_attributes = True


class NBATeam(NBATeamBase):
    id: int

    class Config:
        from_attributes = True


class NBAStandingsBase(BaseModel):
    wins: int
    losses: int
    winnings_percentage: float
    games_back: Optional[str]
    points_percentage_game: float
    opp_points_percentage_game: float

    class Config:
        from_attributes = True


class NBAStandings(NBAStandingsBase):
    id: int
    team: NBATeam

    class Config:
        from_attributes = True
