import pymongo
import pandas as pd
import numpy as np
import os
import json

# Provide the mongodb localhost url to connect python to mongodb.

class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")

env_var = 

client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME ="aps"
COLLECTION_NAME = "sensor"