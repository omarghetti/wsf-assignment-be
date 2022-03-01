from fastapi import FastAPI

app = FastAPI()


@app.get("/players")
async def get_players():
    return {
        "id": "1",
        "name": "Emerson",
        "position": "Goalkeeper",
        "odds": 0.0,
        "margin": 0.0
        }

@app.post("/margins")
async def post_margins():
    return None;