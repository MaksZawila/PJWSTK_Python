# Maksymilian Zawiła s25085 gr.24c

eq = input("Podaj działanie (np. '2 + 2'): ")

parts = eq.split(" ")
if len(parts) < 3:
    exit(-1)
if not (parts[0].isdigit() and parts[2].isdigit()):
    exit(-1)
a = int(parts[0])
b = int(parts[2])
sym = parts[1]
if sym == '+':
    print(a+b)
elif sym == '-':
    print(a-b)
elif sym == '*':
    print(a*b)
elif sym == '/':
    if b != 0:
        print(a/b)
    else:
        print("Sorki, przez zero sie nie dzieli koleszko")
