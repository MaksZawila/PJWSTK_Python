# Maksymilian Zawiła s25085 gr.24c

class Person:
    def __init__(self, firstname, lastname, gender, date_of_birth):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.date_of_birth = date_of_birth

    def wyswietl_info(self, format='slownik'):
        print(self.get_info(format))
    def get_info(self, format):
        if format == 'lista':
            res = [self.firstname, self.lastname, self.gender, self.date_of_birth]
        elif format == 'krotka':
            res = (self.firstname, self.lastname, self.gender, self.date_of_birth)
        else:
            res = {'Imię': self.firstname, 'Nazwisko': self.lastname, 'Płeć': self.gender,
                    'Data urodzenia': self.date_of_birth}
        return res

    @staticmethod
    def wyswietl_osoby(people):
        return [person.wyswietl_info() for person in people]


class Player(Person):
    def __init__(self, nick, type, email, firstname, lastname, gender, date_of_birth):
        super().__init__(firstname, lastname, gender, date_of_birth)
        self.nick = nick
        self.type = type
        self.email = email

    def wyswietl_info(self, format='slownik'):
        info = super().get_info(format=format)
        info.update({'Nick': self.nick, 'Typ': self.type, 'Email': self.email})
        print(info)

    @staticmethod
    def wyswietl_graczy(players):
        return [player.wyswietl_info() for player in players]


player = Player("Maciek123", "NPC", "mail@mail.com", "Maciek", "Zawierucha", "Kobieta", "30.02.1999")


player.wyswietl_info()
