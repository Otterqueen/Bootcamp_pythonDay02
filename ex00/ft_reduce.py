def ft_reduce(function_to_apply, list_of_inputs):
    to_ret = list_of_inputs[0]
    for item in list_of_inputs[1:]:
        to_ret = function_to_apply(to_ret, item)
    return to_ret


print(ft_reduce(lambda a, b: a + b, range(1, 11)))
