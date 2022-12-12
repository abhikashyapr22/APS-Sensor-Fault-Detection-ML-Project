import pymongo
import pandas as pd
import numpy as np
import os
import json
from dataclasses import dataclass

# Provide the mongodb localhost url to connect python to mongodb.

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    aws_access_key_id: str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_access_secret_key:str = os.getenv("AWS_SECRET_ACCESS_KEY")


env_var = EnvironmentVariable()
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
TARGET_COLUMN = "class"

DATABASE_NAME ="aps"
COLLECTION_NAME = "sensor"