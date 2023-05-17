# Maksymilian Zawiła s25085 gr.24c

import random

random.seed(12)
items = ['python', 'java', 'sql', 'c++', 'c']

n = random.randint(0, len(items) - 1)
print(items[n])
