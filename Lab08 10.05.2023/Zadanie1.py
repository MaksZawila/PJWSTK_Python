a = float(input("Podaj współczynnik a:"))
if a == 0:
    print("Współczynnik a, musi być różny od 0")
    exit(-1)
b = float(input("Podaj współczynnik b:"))
c = float(input("Podaj współczynnik c:"))

delta = b**2-4*a*c
sqrt_delta = delta ** (1/2)
x1 = (-b + sqrt_delta)/2*a
x2 = (-b - sqrt_delta)/2*a

print(x1, x2)