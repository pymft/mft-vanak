vals = [('*', (1, 2)), ('$', (4, 2)), ('%', (56, 3))]


for pat, (x, y) in vals:
    print((x*pat + '\t') * y)
