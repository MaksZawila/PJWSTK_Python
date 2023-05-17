# Maksymilian Zawiła s25085 gr.24c

import re

raw_text = "Wyślij email na adres: info@template.com lub sales-info@template.it"
x = re.findall("[A-Za-z]+[._\-]*[A-Za-z]+@[A-Za-z]+\.[A-Za-z]+", raw_text)
print(x)
