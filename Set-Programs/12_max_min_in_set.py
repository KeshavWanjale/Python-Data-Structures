def get_max_min(my_set):
    return max(my_set), min(my_set)


my_set = {1,2,3,4,5,6,7,8}
max, min = get_max_min(my_set)
print(f"Max : {max}, Min : {min}")