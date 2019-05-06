def echo(s):
    return s


def echo_multiple_times(s, n):
    return echo(s) * n


def get_echoer(n):
    def f(s):
        return echo_multiple_times(s, n)
    return f


echo_twice = get_echoer(2)
# def echo_twice(s):
#     return echo_multiple_times(s, 2)

echo_10 = get_echoer(10)
# def echo_10(s):
#     return echo_multiple_times(s, 10)

print(echo("hello"))
print(echo_twice("hello"))
print(echo_10("hello"))