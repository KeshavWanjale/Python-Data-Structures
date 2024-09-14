def print_table(dictionary):
    print("Key\tValue")
    print("----\t-----")
    for key, value in dictionary.items():
        print(f"{key}\t{value}")

dictionary = {1: 10, 2: 20}
print_table(dictionary)