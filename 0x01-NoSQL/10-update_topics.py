#!/usr/bin/env python3
""" mongodb """


def update_topics(mongo_collection, name, topics):
    """ Updates the topics in the collection """
    mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}})

