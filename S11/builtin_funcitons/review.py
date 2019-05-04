lst = []

lst = [(100, 456), (100, 10000), (2, 34565), (6, 34), (34, 34), (4, 45)]

f = lambda x: x[1]//x[0]
# diff = [f((100, 456)), f((100, 10000)), f((2, 34565)), f((6, 34)), f((34, 34)), f((4, 45))]
# diff = [f(lst[0]), f(lst[1]), f(lst[2]), f(lst[3]), f(lst[4]), f(lst[5])]
# print(diff)

#
# diff = []
#
# for value in lst:
#     tmp = f(value)
#     diff.append(tmp)
#
# print(diff)
# mx = max(diff)
# indx = diff.index(mx)
#
# my_max = lst[indx]
# print(my_max)

value = max(lst, key=f)
print(value)
