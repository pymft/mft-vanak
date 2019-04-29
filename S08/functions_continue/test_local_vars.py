x = 10000


def fun(lst):  # x = 9
    a = 100
    b = 200

    lst.pop(0)
    return lst


list_new = [1, 2, 3, 4]
print(list_new)
list_modified = fun(list_new)
print(list_modified)
print(list_new)



