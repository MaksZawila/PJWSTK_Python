# Maksymilian Zawiła s25085 gr.24c

import pickle

ids = ['001', '003', '011']

with open('C:\\Users\\S25085\\Desktop\\PJWSTK_Python\\Lab09 17.05.2023\\data.pickle', 'wb') as file:
    pickle.dump(ids, file)
