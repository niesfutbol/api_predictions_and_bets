from fastapi import FastAPI
import json
import pandas as pd

premier_league = pd.read_csv("./data/predictions_39_2023_0.csv.csv")
serie_a = pd.read_csv("./data/predictions_135_2023_0.csv.csv")
bets = pd.concat([premier_league, serie_a], ignore_index=True).sort_values(by=['date'])

app = FastAPI()


@app.get("/v1/predictions")
def get_predictions():
    return bets.to_dict(orient="records")
