def remove_items(input_set, items_to_remove):
    input_set.difference_update(items_to_remove)
    return input_set

my_set = {1,2,3,4,5,6,7,8}
remove_items(my_set,{7,8,9,10})
print(my_set)
remove_items(my_set,[5,6,7,8])
print(my_set)