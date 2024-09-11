def add_ly_ing(str):
    if len(str) >= 3:
        if(str.endswith("ing")):
            return str + "ly"
        else:
            return str + "ing"
    else:
        return str
    

print(add_ly_ing("string"))