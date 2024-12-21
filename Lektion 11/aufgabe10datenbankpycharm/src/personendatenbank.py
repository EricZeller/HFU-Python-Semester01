from datetime import date
import json


class Person:
    def __init__(self, fname, lname, bday):
        self.__fname = fname  # schreibgeschützt durch __...
        self.__lname = lname
        self.__bday = date.fromisoformat(bday)

    @property  # so nun als getter markiert
    def fname(self):
        return self.__fname

    @property
    def lname(self):
        return self.__lname

    @property
    def bday(self):
        return self.__bday

    def __str__(self):
        return f"{self.__fname} {self.__lname} (geb. {self.__bday})"

    def naechster_geburtstag(self):
        if self.bday.month >= date.today().month and self.bday.day >= date.today().day:
            nextbday = self.__bday.replace(year=date.today().year)
        else:
            nextbday = self.__bday.replace(year=date.today().year + 1)
        return nextbday


class Personendatenbank:
    def __init__(self):
        self.__pliste = []

    def leeren(self):
        self.__pliste.clear()

    def einfuegen(self, nperson):
        for p in self.__pliste:
            if p.fname == nperson.fname and p.lname == nperson.lname:
                raise ValueError(f"Person mit dem Vornamen {nperson.fname} und dem Nachnamen {nperson.lname} ist bereits in der Datenbank vorhanden!")
        self.__pliste.append(nperson)

    def lade(self, datei):
        jsonliste = json.load(datei)
        for line in jsonliste:
            neueperson = Person(
                line['fname'],
                line['lname'],
                line['bday']
            )
            self.einfuegen(neueperson)
        print(f"{len(jsonliste)} Person/en eingelesen.")

    def speichere(self, datei):
        zuspeichern = []
        for person in self.__pliste:
            eintrag = {
                'fname': person.fname,
                'lname': person.lname,
                'bday': person.bday.isoformat()
            }
            zuspeichern.append(eintrag)
        print(f"Speichere {len(zuspeichern)} Person/en...")
        json.dump(zuspeichern, datei, indent=4)

    def findePerson(self, sfname, slname):
        for p in self.__pliste:
            if p.fname == sfname and p.lname == slname:
                return p
        return None

    def naechste_geburtstage(self):
        naechste_geburtstage = self.__pliste
        naechste_geburtstage = sorted(naechste_geburtstage, key=Person.naechster_geburtstag)
        return naechste_geburtstage