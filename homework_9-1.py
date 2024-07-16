def apply_all_func(int_list, *functions):
    results = {funk.__name__: funk(tuple(int_list)) for funk in functions}
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


