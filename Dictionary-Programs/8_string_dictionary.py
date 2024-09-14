def character_frequency(str):
    # Convert the string to lowercase to make the count case-insensitive
    str = str.lower()
    frequency = {}
    for char in str:
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1

    return frequency


str = "w3resource"

frequency = character_frequency(str)
print(frequency)