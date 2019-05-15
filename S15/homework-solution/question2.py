def describe_duration(t):
    if t < 0.3:
        return "S"
    elif t > 1.0:
        return "L"
    else:
        return "M"


# LSSL LSSSL LSSSSL


data = [0.0, 0.7, 1.1, 2.9, 3.1, 3.4, 4.6, 4.7, 5.0, 5.3, 9.0]
# data[:-1]    [0.0, 1.1, 2.9, 3.1, 3.4, 5.0,]
# data[1:]     [1.1, 2.9, 3.1, 3.4, 5.0, 5.2]


# duration = []
# for i in range(len(data)-1):
#     tmp = data[i+1] - data[i]
#     duration.append(tmp)

# print(duration)

# zip(starts, stops)
periods = zip(data[:-1], data[1:])
# duration = map(lambda a: a[1]-a[0], periods)
durations = [b-a for a, b in periods]
print(durations)

descriptions = [describe_duration(t) for t in durations]
print(descriptions)
line = "".join(descriptions)
print(line)