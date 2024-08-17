my_tuple = ('apple', 'banana', 'cherry')
try:
    my_tuple[1] = 'orange'
except TypeError:
    print("Cannot modify a tuple")
