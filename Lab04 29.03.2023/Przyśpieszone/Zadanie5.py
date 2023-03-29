x = 0
while x <= 0:
    x = input("Podaj liczbę naturalną: ")
    if not x.isdigit():
        x = 0
        continue
    x = int(x)
