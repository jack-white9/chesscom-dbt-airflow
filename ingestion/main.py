import pandas as pd
from chessdotcom import get_leaderboards, Client


def ingest_data():
    Client.request_config["headers"]["User-Agent"] = "a" "b"
    response = get_leaderboards()
    data = response.json["leaderboards"]["live_blitz"]
    df = pd.DataFrame.from_dict(data)
    print(df)


if __name__ == "__main__":
    ingest_data()
