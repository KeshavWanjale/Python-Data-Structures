def common_element(list1,list2):
    for elem in list1:
        if elem in list2:
            return True
    
    else:
        return False

list1 = [1,2,3,45,4]
list2 = [5,6,7,8,9,10,4]

print(common_element(list1,list2))