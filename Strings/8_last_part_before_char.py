def last_par_before_char(str, char):
    return str.split(char)[0]


str = "https://www.w3resource.com/python-exercises/"
print(last_par_before_char(str,"."))