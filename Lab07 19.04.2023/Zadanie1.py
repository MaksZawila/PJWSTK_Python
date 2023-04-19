# Maksymilian Zawiła s25085 gr.24c

class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price


products = []
product_properties = ["nazwa", "ilosc", "cena"]
choose = "0"


def print_products():
    print("NR", end="\t")
    for product_property in product_properties:
        print(product_property.upper(), end="\t")
    print()
    for i, product in enumerate(products):
        print(i + 1, end="\t")
        print(product.name, end="\t")
        print(product.amount, end="\t")
        print(product.price, end="\n")


while choose != "5":
    print("1. Dodaj produkt")
    print("2. Usun produkt")
    print("3. Wyswietl produkt")
    print("4. Modyfikuj produkt")
    print("5. Wyjdz")
    choose = input("Wybierz opcję: ")
    print()
    match choose:
        case "1":
            product = {}
            for product_property in product_properties:
                val = input(f"{product_property.capitalize()} produktu: ")
                product[product_property] = val
            products.append(Product(product["nazwa"], product["ilosc"], product["cena"]))
            print("Produkt dodany.")
        case "2":
            print_products()
            index = input("Podaj numer produktu: ")
            if index.isdigit() and int(index) in range(1, len(products) + 1):
                products.pop(int(index) - 1)
        case "3":
            print_products()
        case "4":
            print_products()
            index = input("Podaj numer produktu: ")
            if index.isdigit() and int(index) in range(1, len(products) + 1):
                product = products[int(index) - 1]
                print("Jesli nie chcesz zmieniac wartosci, nic nie wpisuj i kliknij Enter")
                val = input(f"Nazwa produktu. {product.name} => ")
                if len(val):
                    product.name = val
                val = input(f"Ilosc produktu. {product.amount} => ")
                if len(val):
                    product.amount = val
                val = input(f"Cena produktu. {product.price} => ")
                if len(val):
                    product.price = val
                products[int(index) - 1] = product
    print()
