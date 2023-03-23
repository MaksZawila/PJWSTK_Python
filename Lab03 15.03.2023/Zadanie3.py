# Maksymilian Zawiła s25085 24c.

n = ""

while not n.isdigit():
    n = input("Podaj rozmiar tabliczki: ")

n = int(n)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end="\t")
    print()
