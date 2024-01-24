#!/usr/bin/env python3
""" mongodb """


def insert_school(mongo_collection, **kwargs):
    """ insert a new school """
    query = mongo_collection.insert_one(kwargs)

    return query.inserted_id
