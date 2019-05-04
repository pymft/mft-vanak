def word_map(text):
    words = text.lower().split()
    uniques = set(words)
    res = {}

    for u in uniques:
        res[u] = words.count(u)
        # res.update({u: words.count(u)})

    return res


f = open("input.txt", mode="r", encoding="utf-8")
poem = f.read()
f.close()

print(poem.splitlines())
# res = word_map(poem)
# print(res)