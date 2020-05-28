def ft_map(function_to_apply, list_of_inputs):
    list_to_ret = []
    for item in list_of_inputs:
        list_to_ret.append(function_to_apply(item))
    return list_to_ret


print(ft_map(str.upper, ["aaaa", "coucou"]))
