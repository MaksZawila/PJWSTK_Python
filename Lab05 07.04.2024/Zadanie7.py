k = int(input("Podaj k: "))
for i in range(20, 81):
    if i % k == 0:
        print(i, sep=" ")