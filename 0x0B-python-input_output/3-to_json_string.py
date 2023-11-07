#!/usr/bin/python3
''' function that returns the JSON representation'''

import json

def to_json_string(my_obj):
    '''returns JSON representation'''
    return json.dumps(my_obj)
