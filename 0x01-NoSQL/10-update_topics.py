def update_topics(mongo_collection, name, topics):
    query = mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
    
    return query.modified_count