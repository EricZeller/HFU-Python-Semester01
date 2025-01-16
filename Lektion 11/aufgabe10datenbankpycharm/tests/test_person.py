from src.personendatenbank import Person
from datetime import date

def test_naechster_geburtstag_heute():
    person = Person("John", "Cena", "2004-01-01")
    assert person.naechster_geburtstag() == date(year=date.today().year+1, month=1, day=1)