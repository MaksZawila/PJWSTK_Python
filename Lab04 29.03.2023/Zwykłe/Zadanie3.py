def intput(text):
    a = ""
    while not a.isdigit():
        a = input(text)
        if not a.replace("-", "").isdigit():
            print("Wprowadzona wartość jest niepoprawna")
            continue
        return int(a)


n = intput("Podaj liczbe: ")

for i in range(1, n+1):
    if not n%i:
        print(i)
