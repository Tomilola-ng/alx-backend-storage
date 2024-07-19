#!/usr/bin/env python3
""" RISK CHECKER ERROR BOT """

def insert_school(mongo_collection, **kwargs):
    """ KY WORD ARGUMENTS BY PASS """
    response = mongo_collection.insert_one(kwargs)
    return response.inserted_id
