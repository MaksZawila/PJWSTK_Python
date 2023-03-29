def intput(text):
    a = ""
    while not a.isdigit():
        a = input(text)
        if not a.replace("-", "").isdigit():
            print("Wprowadzona wartość jest niepoprawna")
            continue
        return int(a)


n = intput("Podaj n: ")
m = intput("Podaj m: ")

for i in range(0, m):
    for j in range(0, n):
        if i == 0 or j == 0 or i == n-1 or j == m-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()