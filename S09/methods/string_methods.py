text = """April is the cruellest month, breeding
Lilacs out of the dead land, mixing
Memory and desire, stirring
Dull roots with spring rain."""

# res = "hello".capitalize()
# res = "hello".upper()
res = text.title()
print(res)
num = text.count("the")
print(num)
indx = text.find("the", 10)
print(indx)

words = text.lower().split()
print(len(words))
uniques = set(words)
print(len(uniques))


value = " hello     ".strip()
print(value)
