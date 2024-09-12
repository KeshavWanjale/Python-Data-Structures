def find_min(list):
    min = list[0]
    for num in list:
        if num < min:
            min = num
    
    return min


list = [10,11,12,-1,2,3,4]
print(find_min(list))