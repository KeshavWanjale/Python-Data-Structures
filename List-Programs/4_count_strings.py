def count_string(list):
    count = 0
    for elem in list:
        if len(elem) >=2 and elem[0] == elem[-1]:
            count += 1
    
    return count


list = ['abc', 'xyz', 'aba', '1221']
print(count_string(list))