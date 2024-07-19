#!/usr/bin/env python3
""" PY MONGO FOR MY HEAD LIKE CRAZY """


def list_all(mongo_collection):
    """ FUNC TO ILST ALL DOCS """
    return list(mongo_collection.find())
