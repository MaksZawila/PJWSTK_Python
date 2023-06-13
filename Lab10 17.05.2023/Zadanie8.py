# Maksymilian Zawiła s25085 gr.24c
import json

stocks = {'PLW': 360.0, 'TEN': 320.0, 'CDR': 329.0}
print(json.dumps(stocks, sort_keys=True))
