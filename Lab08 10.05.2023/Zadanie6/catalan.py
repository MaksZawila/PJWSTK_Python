def catalan(n):
    if n <= 1:
        return 1
    x = 0
    for i in range(n):
        x += catalan(i) * catalan(n-1-i)
    return x