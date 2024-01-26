#!/usr/bin/env python3
""" mongodb """


def top_students(mongo_collection):
    """ return a list of top students """
    pipeline = [
        {
            "$group": {
                "_id": "$_id",
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    return list(mongo_collection.aggregate(pipeline))
