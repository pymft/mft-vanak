def find_all(text, pat):
    out = []
    start = 0
    while True:
        indx = text.find(pat, start)
        start = indx + 1
        if start == 0:
            return out
        out.append(indx)




text = "hello hello aaa hello "
res = find_all(text, "hello")
print(res)