#!/usr/bin/env python3
""" MY FAITH DEPENDS ON THIS """


def update_topics(mongo_collection, name, topics):
    """ IT DEY SHAKE OO """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_values)
