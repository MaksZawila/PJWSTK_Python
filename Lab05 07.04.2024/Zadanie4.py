price_before = [3.69, 4.5, 3.6, 4.0, 3.99, 3.59]
price_after = [4.5, 5.5, 4.69, 4.99, 4.00]
print("Najwyższa cena po nałożeniu podatku: ", max(price_after))
print("Najniższa cena coli w historii: ", min(price_after + price_before))
print("Średnia cena przed podwyżką cen: ", sum(price_before)/len(price_before))
print("Średnia cena przed podwyżką cen: ", sum(price_after)/len(price_after))