def count_sub_str(main_string,substring):
    count = 0
    sub_len = len(substring)
            
    for i in range(len(main_string) - sub_len + 1):
        if main_string[i:i+sub_len] == substring:
            count += 1
    
    return count


str = "abcdabefabghab"
print(count_sub_str(str,"ab"))