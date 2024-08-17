my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
try:
    my_list.append(4)
    print("List after append:", my_list)
except AttributeError:
    print("Cannot append to a tuple")

try:
    my_tuple.append(4)
except AttributeError:
    print("Cannot append to a tuple")
