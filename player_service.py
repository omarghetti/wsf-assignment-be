import string
from tinydb import TinyDB, Query

db = TinyDB('db.json')
db.truncate()

db.insert({"id": "1", "name": "Emerson","position": "Goalkeeper","odds": 0.76,"margin": 0.23})
db.insert({"id": "2", "name": "Jonh Terry","position": "Defender","odds": 0.54,"margin": 0.21})
db.insert({"id": "3", "name": "Joe Cole","position": "Midfielder","odds": 0.32,"margin": 0.32})
db.insert({"id": "4", "name": "Falcao","position": "Defender","odds": 0.43,"margin": 0.28})
db.insert({"id": "5", "name": "Alexandre Pato","position": "Forward","odds": 0.78,"margin": 0.11})


def get_all_players():
    return db.all()

def update_player_margin(id: string):
    return None
