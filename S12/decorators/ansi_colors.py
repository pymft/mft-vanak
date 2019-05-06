def red(f):
    inner = lambda *args: "\033[31;1m" + str(f(*args)) + "\033[0m"
    return inner


def add_stars(f):
    def inner(*args):
        return "*" + str(f(*args)) + "*"

    return inner

def green(f):
    def inner(*args):
        return "\033[32;1m" + str(f(*args)) + "\033[0m"

    return inner


@green   # echo = green(echo)
def echo(s):
    return s


def make_mirrors(inp):
    lst = list(inp)
    mid = len(lst) // 2
    left = lst[:mid]

    if len(lst) % 2 == 0:
        center = []
        right = lst[mid:]
    else:
        center = [lst[mid]]
        right = lst[mid+1:]

    left_mirror = left + center + left[::-1]
    right_mirror = right[::-1] + center + right

    return left_mirror


green(add_stars(echo))("hello")
print(make_mirrors([1,2, 3,4, 5, 6]))

# echo = add_stars(echo)


print(echo("hello"))
