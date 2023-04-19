# Maksymilian Zawiła s25085 gr.24c

def catalan(n):
    if n <= 1:
        return 1
    x = 0
    for i in range(n):
        x += catalan(i) * catalan(n-1-i)
    return x


def print_catalana(n, mode):
    i = 0
    c = catalan(i)
    while c < n:
        if mode == "p" and c % 2 == 0:
            print(c)
        if mode == "n" and c % 2 == 1:
            print(c)
        if mode == "a":
            print(c)
        i += 1
        c = catalan(i)


print_catalana(1000000, "a")
