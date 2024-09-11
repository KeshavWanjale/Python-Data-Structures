def length_of_longest_word(words):
    max_len = 0
    for i in range(len(words)):
        curr_len = len(words[i])
        if curr_len > max_len:
            max_len = curr_len

    return max_len

words = ["Kes","Kesh","keshav"]

print(length_of_longest_word(words))