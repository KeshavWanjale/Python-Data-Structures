def remove_duplicates(list_of_lists):
    unique_elem = []
    for sublist in list_of_lists:
        for element in sublist:
            if element not in unique_elem:
                unique_elem.append(element)
            else:
                sublist.remove(element)

    return list_of_lists


list_of_lists = [[1, 2, 3, 4], [5, 5, 6, 7], [1, 8, 9, 10]]
print(remove_duplicates(list_of_lists))