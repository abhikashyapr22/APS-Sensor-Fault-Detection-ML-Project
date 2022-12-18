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


# env_var = EnvironmentVariable()
# mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
# TARGET_COLUMN = "class"

env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient("mongodb+srv://root:abhi123@cluster0.rzyk2u3.mongodb.net/?retryWrites=true&w=majority")
TARGET_COLUMN = "class"

# DATABASE_NAME ="aps"
# COLLECTION_NAME = "sensor"