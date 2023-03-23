# Maksymilian Zawiła s25085 24c.

def catalan(x):
    if x <= 1:
        return 1
    res = 0
    for i in range(x):
        res += catalan(i) * catalan(x - i - 1)
    return res


n = ""
while not n.isdigit():
    n = input("Podaj liczbe: ")
n = int(n)

j = 0

print("Liczby Catalana: ", end="")

while catalan(j) < n:
    print(catalan(j), end=" ")
    j += 1
