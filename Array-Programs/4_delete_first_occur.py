import array


def delete_first_occurrence(arr,element):
    for elem in arr:
        if elem == element:
            arr.remove(elem)
            break
    return arr

arr = array.array('i',[1,2,3,4,5,5,6,7,5])
element = 5
print(delete_first_occurrence(arr,element))