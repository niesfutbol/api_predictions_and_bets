from fastapi import FastAPI
import json
import players_from_as as pfa


f = open("./players.json")
players = json.load(f)
PLAYERS = pfa.get_player_info_from_list(players["response"])

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/make_add")
def make_add():
    return {"add": 4 + 6}


@app.get("/all_bd")
def get_all_items():
    base_datos = pd.read_csv(PATH_DATABASE)
    return base_datos.to_dict()

@app.get("/player/{player_id}")
def get_player(player_id: int):
    return PLAYERS[player_id]