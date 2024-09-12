def remove_duplicates(list):
    unique_list = []
    for elem in list:
        if elem not in unique_list:
            unique_list.append(elem)

    return unique_list


list = [1,1,'a','a','b','c',"hello","hello"]
print(remove_duplicates(list))