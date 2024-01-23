from typing import List, Dict, Union

def list_all(mongo_collection) -> List[Dict[str, Union[str, int]]]:
    """ List all documents in a MongoDB collection. """
    return list(mongo_collection.find())