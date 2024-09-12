def multiply_all_elements(list):
    mul = 1
    for num in list:
        mul *= num

    return mul


list = [10,10,30,50]
print(multiply_all_elements(list))