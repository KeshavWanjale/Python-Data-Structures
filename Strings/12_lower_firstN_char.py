def lower_first_n(str,n):
    return str[:n+1].lower()+str[n+1::]


str = "ABCDefghi"
print(lower_first_n(str,4))