def make_mirrors(inp):
    lst = list(inp)
    mid = len(lst) // 2
    left = lst[:mid]

    if len(lst) % 2 == 0:
        center = []
        right = lst[mid:]
    else:
        center = [lst[mid]]
        right = lst[mid+1:]

    left_mirror = left + center + left[::-1]
    right_mirror = right[::-1] + center + right

    return left_mirror, right_mirror


lst = (1, 2, 3, 4, 5, 6, 7, 8)
left, right = make_mirrors(lst)
print(left)
print(right)
print(lst)