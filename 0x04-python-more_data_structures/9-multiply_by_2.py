#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    tmp_dict = a_dictionary.copy()
    for i in tmp_dict.keys():
        tmp_dict[i] *= 2
    return tmp_dict
