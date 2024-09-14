sample_dict = {1: 30, 2: 20, 3: 10}

def value(item):
    # print(item[1]) 0 is key and 1 is value
    return item[1] 

sorted_dict_asc = dict(sorted(sample_dict.items(),key=value))
sorted_dict_dec = dict(sorted(sample_dict.items(),key=value, reverse=True))

print("Ascending order:", sorted_dict_asc)
print("Descending order:", sorted_dict_dec)