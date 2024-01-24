#!/usr/bin/env python3
""" mongodb """


def schools_by_topic(mongo_collection, topic):
    """ return a list of instances of
      the specified topic """
    return mongo_collection.find({"topics": topic})
