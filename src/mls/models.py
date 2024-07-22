from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from src.core.models import Team, Standings


class MLSTeam(Team):
    __tablename__ = 'mls_teams'
    team_logo = Column(String)
    standings = relationship("MLSStandings", back_populates="team", uselist=False)


class MLSStandings(Standings):
    __tablename__ = 'mls_standings'
    team_id = Column(Integer, ForeignKey('mls_teams.id'), unique=True, nullable=False)
    draw = Column(Integer)
    goals_for = Column(Integer)
    goals_against = Column(Integer)
    goal_difference = Column(Integer)
    points = Column(Integer)
    points_per_game = Column(Float)

    team = relationship("MLSTeam", back_populates="standings")
