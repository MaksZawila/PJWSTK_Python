def intput(text):
    x = input(text)
    if x.isdigit() and int(x) > 0:
        return int(x)
    print("Podana liczba powinna być całkowita > 0")
    return intput(text)


a = intput("Podaj pierwszy bok: ")
b = intput("Podaj drugi bok: ")
c = intput("Podaj trzeci bok: ")

if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("Podane liczby są trójkami pitagorejskimi")
else:
    print("Podane liczby nie są trójkami pitagorejskimi")