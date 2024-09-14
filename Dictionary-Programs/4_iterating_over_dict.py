dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# by default only keys
for i in dic1:
    print(i)
# accessing only values
for value in dic1.values():
    print(value)
# accessing both keys and values
for key, value in dic1.items():
    print(f'Key: {key}, Value: {value}')