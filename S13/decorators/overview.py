def decorator(f):
    def inner(*args):
        return " * " + f(*args) + " * "
    return inner


@decorator
@decorator
def echo(s):
    return s


echo = decorator(decorator(echo))

# new_echo = decorator(echo)
#
# # def new_echo(s):
# #     return echo(s)
#
# print(new_echo("hello"))
#
# echo = decorator(echo)
print(echo("hello"))