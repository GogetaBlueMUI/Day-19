def sort_by_values(d):
    return sorted(((value, key) for key, value in d.items()), reverse=True)

my_dict = {'a': 10, 'b': 1, 'c': 22}
print(sort_by_values(my_dict))
