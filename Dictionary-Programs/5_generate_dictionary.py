def generate_dictionary(N):
    dictionary = {}
    for i in range(1, N+1):
        if i not in dictionary:
            dictionary[i] = i*i

    return dictionary


print(generate_dictionary(5))