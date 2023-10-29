import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from chessdotcom import get_leaderboards, Client


def extract_data():
    Client.request_config["headers"]["User-Agent"] = "a" "b"
    response = get_leaderboards()
    data = response.json["leaderboards"]["live_blitz"]
    df = pd.DataFrame.from_dict(data)
    df = df.drop(labels=["trend_score", "trend_rank"], axis=1)
    df["ingestion_date"] = pd.Timestamp("now")
    return df


def load_data(df):
    load_dotenv()
    PG_USERNAME = os.getenv("PG_USERNAME")
    PG_PASSWORD = os.getenv("PG_PASSWORD")
    PG_HOST = os.getenv("PG_HOST")
    PG_PORT = os.getenv("PG_PORT")
    PG_DATABASE = os.getenv("PG_DATABASE")
    engine = create_engine(
        f"postgresql://{PG_USERNAME}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"
    )
    df.to_sql(name="players", schema="source", con=engine, if_exists="append")
    print("Data loaded.")


def run():
    df = extract_data()
    load_data(df)


if __name__ == "__main__":
    run()
