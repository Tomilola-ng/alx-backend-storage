#!/usr/bin/env python3
""" Pymongo Operations """

from typing import List, Dict


def top_students(mongo_collection) -> List[Dict]:
    """
        Returns all students sorted by average score
    """

    top_students_cursor = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    top_students_list = list(top_students_cursor)
    return top_students_list
