from fastapi import FastAPI
from src.core.routers import router as core_routers
from src.nba.routers import router as nba_routers
from src.mls.routers import router as mls_routers

app = FastAPI(title="LeagueVerse")

app.include_router(core_routers, prefix="/core", tags=["core"])
app.include_router(nba_routers, prefix="/nba", tags=["nba"])
app.include_router(mls_routers, prefix="/mls", tags=["mls"])
