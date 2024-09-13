import array 


def count_occur(arr,elem):
    count = 0
    for i in arr:
        if i == elem:
            count += 1
    return count


arr = array.array('i',[1,2,3,4,5,5,2,5,6,7,3,2,5])
element = 5

print(f'The element {element} occurs {count_occur(arr, element)} times in the array.')