# Maksymilian Zawiła s25085 gr.24c

def sito_eratostenesa_for(n):
    from math import sqrt
    lista_liczb = []
    lista = [0] + (n * [1])
    max_liczba = int(sqrt(n))

    for indeks in range(2,max_liczba+1):
        if lista[indeks]:
            for indeks_2 in range(indeks*indeks,n+1,indeks):
                lista[indeks_2] = 0
    for element in range(2,n+1):
        if lista[element]:
            lista_liczb.append(element)

    print(lista_liczb)

sito_eratostenesa_for(75)