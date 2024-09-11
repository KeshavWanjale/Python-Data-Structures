def replace_char(str):
    first_char = str[0]
    new_str = first_char

    for char in str[1:]:
        if char == first_char:
            new_str += "$"
        else:
            new_str += char

    return new_str


print(replace_char("AbcdAbAbA"))