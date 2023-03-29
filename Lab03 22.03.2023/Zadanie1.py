# Maksymilian Zawiła s25085 24c.

properties_names = ["imie", "data urodzenia", "e-mail", "telefon"]

properties_list = []
properties_tuple = ()
properties_dict = {}
for property_name in properties_names:
    val = input(f"Podaj {property_name}: ")
    properties_list.append(val)
    properties_dict[property_name] = val
    properties_tuple += (val,)

print(f"Lista: {properties_list}")
print(f"Krotka: {properties_tuple}")
print(f"Słownik: {properties_dict}")