# Maksymilian Zawiła s25085 gr.24c

def check_if_perfect(num):
    suma = 0
    for i in range(1, int(num/2)+1):
        if num % i == 0:
            suma += i
    return {num: suma == num}


print(check_if_perfect(6))
