#!/usr/bin/env python3
""" SEE LIFE CODE OO """


def schools_by_topic(mongo_collection, topic):
    """ FAKEST PROGRAMMER """
    documents = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(documents)]
