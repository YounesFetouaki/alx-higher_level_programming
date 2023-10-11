#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None

    highest_score = max(a_dictionary.values())
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value is highest_score:
                return key
