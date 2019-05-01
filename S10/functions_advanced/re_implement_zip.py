

def my_zip(*args):
    list(args)
    size_of_tuples = len(args)
    size = len(args[0])
    i = 0
    lst = []

    while i < size:
        tmp = ()
        for j in range(size_of_tuples):
            tmp += (args[j][i],)
        lst.append(tmp)
        i += 1

    return lst

digits = [1, 2, 3, 4, 5]
english = ['one', 'two', 'three', 'four', 'five']
russian = ['odin', 'dva', 'tri', 'chtri', 'piot']

res  =my_zip(digits, english, russian)
print(res )
