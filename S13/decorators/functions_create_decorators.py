def color(c):
    color_map = {'red': '31', 'purple': '35', 'green': '32', 'yellow':'33'}
    def some_color(f):
        def inner(*args):
            return "\033[{c};1m{val}\033[0m".format(c=color_map[c], val=f(*args))

        return inner

    return some_color


@color('green')
def echo(s):
    return s


# echo = color(31)(echo)

print(echo("hello"))