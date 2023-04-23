a = 3
b = 4
for i in range(a):
    for j in range(b):
        print("*", end="")
    print()
print("Obwód: ", a+a+b+b)
print("Pole: ", a*b)