def split_by_first_character(words_list):
    split_dict = {}
    for word in words_list:
        first_char = word[0]
        if first_char not in split_dict:
            split_dict[first_char] = []
        split_dict[first_char].append(word)
    return split_dict

words_list = ['apple', 'banana', 'apricot', 'blueberry', 'cherry', 'avocado']
split_result = split_by_first_character(words_list)
print(split_result)