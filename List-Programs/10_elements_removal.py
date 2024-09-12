def remove_elem(list):
    for i in [5,4,0]:
        if i < len(list):
            list.pop(i)

    return list


list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(remove_elem(list))