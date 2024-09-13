def find_elem(tuple,value):
    for elem in tuple:
        if(value == elem):
            return True
        
    return False


my_tuple = (1,2,34,5,67,8,9)

print(find_elem(my_tuple,8))
print(find_elem(my_tuple,10))