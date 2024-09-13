def remove_if_present(my_set,item_to_remove):
    my_set.discard(item_to_remove)
    return my_set


my_set = {1,2,3,4,5,6,7,8}

remove_if_present(my_set, 7)
print(my_set)
