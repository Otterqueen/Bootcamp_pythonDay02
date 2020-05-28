def ft_filter(function_to_apply, list_of_inputs):
    list_to_ret = []
    for item in list_of_inputs:
        if(function_to_apply(item)):
            list_to_ret.append(item)
    return list_to_ret


print(ft_filter(str.isdecimal, ["aaaa", "1111", "123aeaze", "2222"]))
