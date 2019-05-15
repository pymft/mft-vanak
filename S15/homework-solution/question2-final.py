def describe_duration(t):
    T1, T2 = 0.3, 1.0
    if t < T1:
        return "S"
    elif t > T2:
        return "L"
    return "M"


def find_all(text, pat):
    out = []
    start = 0
    while True:
        indx = text.find(pat, start)
        start = indx + 1
        if start == 0:
            return out
        out.append(indx)


def find_all_pats(text, pats):
    out = {p: find_all(text, p) for p in pats}
    return out


data = [0.0, 0.7, 1.1, 2.9, 3.1, 3.15, 3.2, 3.4, 4.6, 4.7, 5.0, 5.3, 9.0]

periods = zip(data[:-1], data[1:])
durations = map(lambda x: x[1] - x[0], periods)
descriptions = [describe_duration(t) for t in durations]
line = "".join(descriptions)

print(line)
pats = ["LSL", "LSSL", "LSSSL", "LSSSSL"]
res = find_all_pats(line, pats)
print(res)
