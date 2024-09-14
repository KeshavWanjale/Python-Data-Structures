def key_present(dict, key):
    return all(key in dict.keys() for key in key)


dictionary = {'a': 1, 'b': 2, 'c': 3}
keys = ['a', 'c']
print(key_present(dictionary, keys))

keys = ['a', 'd']
print(key_present(dictionary, keys))