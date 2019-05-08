line = "It's %-20s %s" % ("James", "Bond")

print(line)

line2 = "num=%-10d" % (1000.12312)
print(line2)

line2 = "num=%e" % (1000.12312)
print(line2)


line3 = "num=%10.3f" % (1000.12312)
print(line3)