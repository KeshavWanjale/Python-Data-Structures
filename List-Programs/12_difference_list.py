def list_difference(list1, list2):
    return list(set(list2) - set(list1))


list_1 = [1,2,6]
list_2 = [1,2,3,6,7]

print(list_difference(list_1,list_2))