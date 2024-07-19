from pydantic import BaseModel


class NBATeamBase(BaseModel):
    name: str
    conference: str
    division: str
    team_logo: str


class NBATeamCreate(NBATeamBase):
    pass


class NBATeam(NBATeamBase):
    id: int

    class Config:
        orm_mode = True


class NBAStandingsBase(BaseModel):
    wins: int
    losses: int
    winnings_percentage: float
    games_back: str
    points_percentage_game: float
    opp_points_percentage_game: float


class NBAStandingsCreate(NBAStandingsBase):
    team_id: int


class NBAStandings(NBAStandingsBase):
    id: int
    team: NBATeam

    class Config:
        orm_mode = True
