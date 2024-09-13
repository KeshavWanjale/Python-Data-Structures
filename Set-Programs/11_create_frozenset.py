def create_frozenset(my_set):
    return frozenset(my_set)

my_set = [1,2,3,4,5,6,7,8,9,9,9,9]

my_frozenset = create_frozenset(my_set)

print(my_frozenset)
frozenset[0] = 10
print(my_frozenset)