num = 10

f = lambda y: y ** 2
is_even = lambda n: n % 2 == 0
is_greater_than_five = lambda number: number > 5

print(f(3))
print(is_even(3))
print(is_greater_than_five(3))


word_counter = lambda text: len(text.split())












n = word_counter("hello world, que largo  est el mundo")
print(n)