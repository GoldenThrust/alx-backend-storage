#!/usr/bin/env python3
""" mongodb """


from typing import List, Dict, Union


def insert_school(mongo_collection, **kwargs) -> str:
    """ insert a new school """
    query = mongo_collection.insert_one(kwargs)

    return query.inserted_id
