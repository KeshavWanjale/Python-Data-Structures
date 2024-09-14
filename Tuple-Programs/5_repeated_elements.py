def repeated_items(my_tuple):
    rpeated = set()
    for item in my_tuple:
        if my_tuple.count(item) > 1:
            rpeated.add(item)

    return rpeated

my_tuple = (1, 2, 3, 4, 5, 5, 6, 7, 8, 9,6, 10)
print(repeated_items(my_tuple))