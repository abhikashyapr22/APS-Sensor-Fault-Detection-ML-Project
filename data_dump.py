import pymongo
import pandas as pd
import numpy as np
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME ="aps"
COLLECTION_NAME = "sensor"


if __name__ == "__main__":
    df = pd.read_csv('/config/workspace/aps_failure_training_set1.csv')

    print(df.shape)

    # Converted df to json 
    df.reset_index(drop=True, inplace=True)

    json_record = list(json.load(df.T.to_json()).values())

    print(json_record[0])

    # insert converted json to mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)