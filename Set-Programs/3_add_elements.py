def update_set(my_set,new_elements):
    my_set.update(new_elements)
    return my_set


my_set = {1,2,3,4}

my_set = update_set(my_set,{3,4,5,6})
print(my_set)
my_set = update_set(my_set,[6,7,8])
print(my_set)
# use add() for adding single element
# my_set = update_set(my_set,10)
# print(my_set)