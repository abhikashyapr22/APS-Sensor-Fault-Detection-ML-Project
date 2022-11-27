import pandas as pd

def get_collection_as_dataframe(database_name:str, collection_name:str)->pd.DataFrame:
    """
    Description: 
    """
    
    df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
    logging.info(f"Found columns: {df.columns}")
