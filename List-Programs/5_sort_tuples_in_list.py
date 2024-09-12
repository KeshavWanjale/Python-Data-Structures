def sort_tuples(list_of_tuples):
    return sorted(list_of_tuples, key= lambda tup:tup[-1])


list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort_tuples(list))