rows = 20

for i in range(rows):
    line = "*" * (2 * i - 1)
    aligns = {0: '<', 1: '^', 2: '>'}
    # print("{line:{align}{width}}".format(line=line, width=rows * 2 - 1, align=aligns[i % 3]))
    print("{line:^20}")