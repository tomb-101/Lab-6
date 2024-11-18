def find_maximum_difference(a, b):
    # code implementation here...
    max_a=max(a)
    max_b=max(b)
    if max_a>max_b:
        min_b=min(b)
        maximum=max_a-min_b
    else:
        min_a=min(a)
        maximum=max_b-min_a
    return maximum

# print(find_maximum_difference())