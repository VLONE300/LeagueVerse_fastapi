from typing import Optional
from pydantic import BaseModel


class MLSTeamBase(BaseModel):
    name: str
    conference: Optional[str]
    team_logo: Optional[str]

    class Config:
        from_attributes = True


class MLSTeam(MLSTeamBase):
    id: int

    class Config:
        from_attributes = True


class MLSStandingsBase(BaseModel):
    wins: int
    losses: int
    draws: int
    goals_for: int
    goals_against: int
    goal_difference: int
    points: int
    points_per_game: int

    class Config:
        from_attributes = True


class MLSStandings(MLSStandingsBase):
    id: int
    team: MLSTeam

    class Config:
        from_attributes = True
