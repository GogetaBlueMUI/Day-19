def compare_tuples(t1, t2):
    return [x == y for x, y in zip(t1, t2)]

t1 = (1, 2, 3)
t2 = (3, 2, 1)
print(compare_tuples(t1, t2))
