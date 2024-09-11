def get_unique_words(str):
    words = str.split(',')

    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    
    for i in range(len(unique_words)):
        for j in range(i+1,len(unique_words)):
            if unique_words[i] > unique_words[j]:
                temp = unique_words[i] 
                unique_words[i] = unique_words[j]
                unique_words[j] = temp
    return ', '.join(unique_words)


print(get_unique_words("black, green, red, white, red, green, white"))

