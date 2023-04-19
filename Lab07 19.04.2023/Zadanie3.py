# Maksymilian Zawiła s25085 gr.24c

class Person:
    def __init__(self, firstname, lastname, gender, date_of_birth):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.date_of_birth = date_of_birth


class Player(Person):
    def __init__(self, nick, type, email, firstname, lastname, gender, date_of_birth):
        super().__init__(firstname, lastname, gender, date_of_birth)
        self.nick = nick
        self.type = type
        self.email = email

    def wyswietl_info(self):
        print(vars(self))


player = Player("Maciek123", "NPC", "mail@mail.com", "Maciek", "Zawierucha", "Kobieta", "30.02.1999")


player.wyswietl_info()
