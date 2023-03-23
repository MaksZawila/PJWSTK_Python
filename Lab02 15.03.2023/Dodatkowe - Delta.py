# Maksymilian Zawiła s25085 24c.

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))
delta = b**2-4*a*c
if delta<0:
    print("Delta jest mniejsza od zera")
elif delta>0:
    print("Delta jest większa od zera")
else:
    print("Delta jest równa zero")
print("Delta:", delta)