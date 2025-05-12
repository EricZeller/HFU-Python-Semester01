from src.personendatenbank import Personendatenbank, Person

def test_personendatenbank_einfuegen():
    person = Person("John", "Cena", "2004-01-01")
    datenbank = Personendatenbank()
    datenbank.einfuegen(person)
    assert datenbank.findePerson("John", "Cena").fname == "John"

def test_personendatenbank_naechstegeburtstage():
    person = Person("John", "Cena", "2004-01-01")
    datenbank = Personendatenbank()
    datenbank.einfuegen(person)
    assert len(datenbank.naechste_geburtstage()) == 1


def test_personendatenbank_naechstegeburtstage_len():
    datenbank = Personendatenbank()
    for i in range(10):
        person = Person("John"+str(i), "Cena", "2004-01-01")
        datenbank.einfuegen(person)
    assert len(datenbank.naechste_geburtstage()) == 5