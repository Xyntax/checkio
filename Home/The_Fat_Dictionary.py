# -*- coding: utf-8 -*-

import re

def flatten(dictionary):
    stack = [((), dictionary)]
    #dict result
    result = {}

    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if isinstance(v, dict):
                stack.append((path + (k,), v))
            else:
                result["/".join((path + (k,)))] = v
    return result

# def flatten(s_):
#     s = str(s_).replace('\n','').replace(' ','')
#     print s

# print flatten({"name": {
#                         "first": "One",
#                         "last": "Drone"},
#                     "job": "scout",
#                     "recent": {},
#                     "additional": {
#                         "place": {
#                             "zone": "1",
#                             "cell": "2"}}})