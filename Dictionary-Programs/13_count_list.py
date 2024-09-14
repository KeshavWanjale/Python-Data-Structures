def count_list_in_dict(dict1):
    count = 0
    for value in dict1.values():
        if isinstance(value, list):
            count += len(value)
    return count

dict1 = {1:[1,2,3,4,5], 2:[6,7,8,9], 3:[10,11,],4:12,6:13}

print(count_list_in_dict(dict1)) 