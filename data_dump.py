import pymongo
import pandas as pd
import numpy as np
import json
# from sensor.config import mongo_client

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.rzyk2u3.mongodb.net/?retryWrites=true&w=majority")

DATABASE_NAME ="aps"
COLLECTION_NAME = "sensor"
DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"


if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)

    print(f"Rows and colums: {df.shape}")

    # Converted dataframe to json so that we can dump these record in the mongo db
    df.reset_index(drop=True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    #insert converted json record to mongo db
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)