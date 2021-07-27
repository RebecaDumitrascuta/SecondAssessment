
def my_function(*args, **kwargs):
    my_sum = 0
    if len(args) == 0:
        return my_sum
    else:
        for param in args:
            if isinstance(param, int) or isinstance(param, float):
                my_sum += param
    return my_sum


print(my_function (1, 5, -3, "abc", [12, 56, "cad"]))
print(my_function())
print(my_function (2, 4, "abc", param_1=2))


