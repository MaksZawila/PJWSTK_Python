def intput(text):
    a = 0
    while not a % 2:
        a = input(text)
        if not a.replace("-", "").isdigit() or not int(a) % 2:
            a = 0
            print("Wprowadzona wartość jest niepoprawna")
            continue
        a = int(a)
    return a


x = intput("Podaj x: ")
y = intput("Podaj y: ")
print(f"Suma: {x + y}")
