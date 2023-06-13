# Maksymilian Zawiła s25085 gr.24c

import re

raw_text = "Programowanie w języku Python – od A do Z"
x = re.findall("\S+", raw_text)
print(x)
