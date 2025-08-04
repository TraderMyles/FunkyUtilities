def pipe(value, *funcs):
    for f in funcs:
        value = f(value)
    return value


def flatten(lst):
    return [item for sublist in lst for item in (sublist if isinstance(sublist, list) else [sublist])]

def sum_list(lst):
    return sum(lst)

def flatten_and_sum(data):
    return pipe(data, flatten, sum_list)

def product_list(lst):
    result = 1
    for number in lst:
        result = result * number
    return result

def flatten_and_product(data):
    return pipe(data, flatten, product_list)