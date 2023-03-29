def intput(text):
    a = ""
    while not a.isdigit():
        a = input(text)
        if not a.replace("-", "").isdigit():
            print("Wprowadzona wartość jest niepoprawna")
            continue
        return a


x = intput("Podaj x: ")
print(x[::-1])
