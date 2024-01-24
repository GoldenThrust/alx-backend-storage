from typing import List, Dict, Union

def insert_school(mongo_collection, **kwargs) -> str:
    query = mongo_collection.insert_one(kwargs)

    return query.inserted_id