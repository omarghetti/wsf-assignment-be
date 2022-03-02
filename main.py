from fastapi import FastAPI
from fastapi.responses import JSONResponse
from player_service import get_all_players

app = FastAPI()


@app.get("/players")
async def get_players():
    return JSONResponse(content=get_all_players())

@app.post("/margins")
async def post_margins():
    return None;