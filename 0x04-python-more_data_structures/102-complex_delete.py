#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    copy = a_dictionary.copy()
    for key, v in copy.items():
        if value == v:
            del a_dictionary[key]
    return a_dictionary
