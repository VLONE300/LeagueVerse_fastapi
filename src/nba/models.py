from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from src.core.models import Team, Standings


class NBATeam(Team):
    __tablename__ = 'nba_teams'
    team_logo = Column(String)
    standings = relationship("NBAStandings", back_populates="team", uselist=False)


class NBAStandings(Standings):
    __tablename__ = 'nba_standings'
    team_id = Column(Integer, ForeignKey('nba_teams.id'), unique=True, nullable=False)
    winnings_percentage = Column(Float)
    games_back = Column(String)
    points_percentage_game = Column(Float)
    opp_points_percentage_game = Column(Float)

    team = relationship("NBATeam", back_populates="standings")
