def hanoi(n, A, B, C):
    if n == 1:
        print(A, '--->', C)
    else:
        hanoi(n - 1, A, C, B)
        hanoi(1,     A, B, C)
        hanoi(n-1,   B, A, C)


hanoi(4, 'Tower1', 'Tower2', 'Tower3')
