def len_n_words(list,n):
    n_long_words = []
    for elem in list:
        if len(elem) > n:
            n_long_words.append(elem)

    return n_long_words

    
list = ["Keshav","123456","1234567","abcde"]
print(len_n_words(list,5))