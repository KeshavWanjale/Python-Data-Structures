import array


def print_array(arr):
    for i in range(len(arr)):
        print(f"The element ant index {i} is {arr[i]}")


arr = array.array('i', [1, 2, 3, 4, 5])
print_array(arr)