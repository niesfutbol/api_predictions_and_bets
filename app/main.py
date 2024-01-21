from fastapi import FastAPI
import pandas as pd

def read_data():
    premier_league = pd.read_csv("/app/data/predictions_39_2023_0.csv")
    ligue_1 = pd.read_csv("/app/data/predictions_61_2023_0.csv")
    busdesliga = pd.read_csv("/app/data/predictions_78_2023_0.csv")
    eredivisie = pd.read_csv("/app/data/predictions_88_2023_0.csv")
    primeira_liga = pd.read_csv("/app/data/predictions_94_2023_0.csv")
    serie_a = pd.read_csv("/app/data/predictions_135_2023_0.csv")
    la_liga = pd.read_csv("/app/data/predictions_140_2023_0.csv")
    all_leagues = [premier_league, ligue_1, serie_a, busdesliga, la_liga, eredivisie, primeira_liga]
    all_bets = pd.concat(all_leagues, ignore_index=True).sort_values(by=['date'])
    return all_bets.loc[(all_bets["home"] > 0.55) | (all_bets["away"] > 0.55) | (all_bets["draw"] > 0.55)]


app = FastAPI()


@app.get("/v1/predictions")
def get_predictions():
    bets = read_data()
    return bets.to_dict(orient="records")
