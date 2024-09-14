def get_unique_values(dict_list):
    unique_values = set()

    for dictionary in dict_list:
        for value in dictionary.values():
            unique_values.add(value)

    return unique_values


dict_list = [{'a': 1, 'b': 2}, {'b': 2, 'c': 3}, {'a': 1, 'c': 3}]

unique_values = get_unique_values(dict_list)

print(unique_values) 