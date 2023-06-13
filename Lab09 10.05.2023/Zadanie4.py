# Maksymilian Zawiła s25085 gr.24c

import os

folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')

if not os.path.exists(folder):
    print(f"Folder '{folder}' nie istnieje.")
else:
    elements = os.listdir(folder)

    for el in elements:
        path = os.path.join(folder, el)
        if os.path.isfile(path):
            print(f"{el} - plik")
        elif os.path.isdir(path):
            print(f"{el} - folder")
        else:
            print(f"{el} - nieznany typ")
