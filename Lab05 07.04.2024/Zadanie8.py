n = int(input("Podaj dolny zakres: "))
m = int(input("Podaj górny zakres: "))
k = int(input("Podaj k: "))
for i in range(n, m+1):
    if i % k == 0:
        print(i, sep=" ")