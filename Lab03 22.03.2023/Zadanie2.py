# Maksymilian Zawiła s25085 24c.

values = []


def is_prime(x):
    if x < 0:
        x *= -1
    if x == 0 or x == 1:
        return False
    for i in range(2, x):
        if not x % i:
            return False
    return True


while len(values) < 20:
    val = input(f"{len(values) + 1}. Podaj liczbe z zakresu [-20;20]: ")
    if not val.replace("-", "").isdigit() or int(val) not in range(-20, 21):
        print("Wprowadzono niepoprawna wartosc.")
        continue
    values.append(int(val))

values_copy = values[:]

values_tuple = ()
for value in values:
    if is_prime(value):
        values_tuple += (value,)

print(f"Liczby pierwsze: {values_tuple}")

values_powered = ()
for value in values:
    if not value % 2:
        values_powered += (value ** 2,)

print(f"Kwadraty liczb podzielnych przez 2: {values_powered}")

for i, value in enumerate(values):
    if not value % 2:
        values[i] = "A"

print(f"Po zamianie: {values}")
