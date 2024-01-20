from fastapi import FastAPI
import pandas as pd

def read_data():
    premier_league = pd.read_csv("/app/data/predictions_39_2023_0.csv")
    busdesliga = pd.read_csv("/app/data/predictions_78_2023_0.csv")
    serie_a = pd.read_csv("/app/data/predictions_135_2023_0.csv")
    all_bets = pd.concat([premier_league, serie_a, busdesliga], ignore_index=True).sort_values(by=['date'])
    return all_bets.loc[(all_bets["home"] > 0.55) | (all_bets["away"] > 0.55) | (all_bets["draw"] > 0.55)]
app = FastAPI()


@app.get("/v1/predictions")
def get_predictions():
    bets = read_data()
    return bets.to_dict(orient="records")
