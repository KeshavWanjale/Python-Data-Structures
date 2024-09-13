import array


def get_reverse_array(arr):
    return arr[::-1]

arr = array.array('i',[1,2,3,4,5])

reverse_arr = get_reverse_array(arr)
print(reverse_arr)