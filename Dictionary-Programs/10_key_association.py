def value_associated_key(list_dict):
    count = 0
    # for d in dict_list:
    #     if d.get('success') == True:
    #         count += 1
    for dict in list_dict:
        for key, value in dict.items():
            if key == "success" and value == True:
                count += 1
    return count


list_dict = [{'id': 1, 'success': True, 'name': 'Lary'}, 
             {'id': 2, 'success':False, 'name': 'Rabi'}, 
             {'id': 3, 'success': True, 'name': 'Alex'}]

print(value_associated_key(list_dict)) 