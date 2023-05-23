# Maksymilian Zawiła s25085 gr.24c

import math


def calculate_root(a, b, c):
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return None
    elif delta == 0:
        x = -b / (2 * a)
        return round(x, 2)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return round(x1, 2), round(x2, 2)
