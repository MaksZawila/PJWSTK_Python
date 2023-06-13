# Maksymilian Zawiła s25085 gr.24c

import Kalkulator


def read_numbers():
    while True:
        a = float(input("Podaj liczbę a: "))
        b = float(input("Podaj liczbę b (różną od zera): "))
        if b != 0:
            return a, b
        else:
            print("Liczba b powinna być różna od zera.")


def print_menu():
    print("Menu:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Wyjście")


def calculate(option, a, b):
    if option == 1:
        res = Kalkulator.add(a, b)
        print("Wynik dodawania:", res)
    elif option == 2:
        res = Kalkulator.subtract(a, b)
        print("Wynik odejmowania:", res)
    elif option == 3:
        res = Kalkulator.multiply(a, b)
        print("Wynik mnożenia:", res)
    elif option == 4:
        res = Kalkulator.divide(a, b)
        print("Wynik dzielenia:", res)


while True:
    print_menu()
    choice = int(input("Wybierz opcję: "))

    if choice == 5:
        print("Koniec programu.")
        break

    if choice in [1, 2, 3, 4]:
        nums = read_numbers()
        a, b = nums
        calculate(choice, a, b)
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
