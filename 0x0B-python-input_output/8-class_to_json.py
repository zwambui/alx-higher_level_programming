#!/usr/bin/python3
"""module 8-class_to_json
 returns the dictionary description with simple data structure
 (list, dictionary, string, integer and boolean)
 for JSON serialization of an object:
"""


def class_to_json(obj):
    """
     returns the dictionary description with simple data structure
    """

    return obj.__dict__
