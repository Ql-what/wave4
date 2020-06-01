def fun(dictionary, lookup_value):
    keys = [key for key, value in dictionary.items() if value == lookup_value]
    return keys