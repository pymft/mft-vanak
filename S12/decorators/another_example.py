def echo(s):
    return str(s)


def say_hello(name):
    return "hello " + name


def say_something():
    return "something"

#
# def add_stars(f):
#     inner = lambda s: "*" + f(s) + "*"
#     return inner

def add_stars(f):
    def inner(*args):
        return "*" + str(f(*args)) + "*"
    return inner


new_echo = add_stars(echo)
new_say_hello = add_stars(say_hello)
new_say_something = add_stars(say_something)

print(new_echo("hello"))
print(new_say_hello("John"))
print(new_say_something())

# print(add_stars(echo, "hello"))
# print(add_stars(say_hello, "John"))
#
# print(echo("hello"))
# print(say_hello("John"))
# print(say_something())