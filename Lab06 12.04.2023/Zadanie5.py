# Maksymilian Zawiła s25085 24c.

products = []
product_properties = ["nazwa", "ilosc", "cena"]
choose = "0"


def add():
    product = {}
    for product_property in product_properties:
        val = input(f"{product_property.capitalize()} produktu: ")
        product[product_property] = val
    products.append(product)
    print("Produkt dodany.")


def delete():
    index = input("Podaj numer produktu: ")
    if index.isdigit() and int(index) in range(1, len(products) + 1):
        products.pop(int(index) - 1)


def print_products():
    print("NR", end="\t")
    for product_property in product_properties:
        print(product_property.upper(), end="\t")
    print()
    for i, product in enumerate(products):
        print(i + 1, end="\t")
        for value in product.values():
            print(value, end="\t")
        print()


def modify():
    index = input("Podaj numer produktu: ")
    if index.isdigit() and int(index) in range(1, len(products) + 1):
        product = products[int(index) - 1]
        print("Jesli nie chcesz zmieniac wartosci, nic nie wpisuj i kliknij Enter")
        for key, value in product.items():
            val = input(f"{key.capitalize()} produktu. {value} => ")
            if len(val):
                product[key] = val
        products[int(index) - 1] = product


while choose != "5":
    print("1. Dodaj produkt")
    print("2. Usun produkt")
    print("3. Wyswietl produkt")
    print("4. Modyfikuj produkt")
    print("5. Wyjdz")
    choose = input("Wybierz opcję: ")
    print()
    match (choose):
        case "1":
            add()
        case "2":
            print_products()
            delete()
        case "3":
            print_products()
        case "4":
            print_products()
            modify()
    print()
