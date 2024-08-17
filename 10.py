def reversed_sorted_tuples(d):
    return sorted(((value, key) for key, value in d.items()))

my_dict = {'a': 10, 'b': 1, 'c': 22}
print(reversed_sorted_tuples(my_dict))
