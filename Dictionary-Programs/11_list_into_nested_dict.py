def list_into_nested_dict(list1):
    nested_dict = current = {}
    for item in list1:
        # print(nested_dict)
        # print(current)
        current[item] = {}
        # putting current inside nested dict 
        current = current[item]
    
    return nested_dict


list1 = ['a', 'b', 'c', 'd', 'e']

nested_dict = list_into_nested_dict(list1)
print(nested_dict)