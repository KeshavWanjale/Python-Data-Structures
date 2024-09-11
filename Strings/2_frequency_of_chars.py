def freq_of_chars(str):
    freq = {}
    for char in str:
        if char in freq:
            # if present then add 1 to count
            freq[char] += 1
        else:
            # if char not present in dict then intialize with key =1
            freq[char] = 1
    return freq

print(freq_of_chars("abcdeabcd"))