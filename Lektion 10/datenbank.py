from datetime import date
import json

class Person:
    def __init__(self, fname, lname, bday):
        self.__fname = fname #schreibgeschützt durch __...
        self.__lname = lname
        self.__bday = date.fromisoformat(bday)

    @property # so nun als getter markiert
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
    
class Personendatenbank:
    def __init__(self):
        self.__pliste = []
    
    def leeren(self):
        self.__pliste.clear()
    
    def einfuegen(self, nperson):
        self.__pliste.append(nperson)

    def lade(self, datei):
        jsonListe = json.load(datei)
        for line in jsonListe:
            neueperson = Person(
                line['fname'], 
                line['lname'], 
                line['bday']
            )
            self.einfuegen(neueperson)
        print(f"{len(jsonListe)} Person/en eingelesen.")

    def speichere(self, datei):
        zuSpeichern = []
        for person in self.__pliste:
            eintrag = {
                'fname': person.fname,
                'lname': person.lname,
                'bday': person.bday.isoformat()
            }
            zuSpeichern.append(eintrag)
        json.dump(zuSpeichern, datei, indent=4)
    
    def findePerson(self, sfname, slname):
        for p in self.__pliste:
            if p.fname == sfname and p.lname == slname:
                return p
        return None

def mainloop():
    datenbank = Personendatenbank()
    while True:
        print("\nWähle eine Option:")
        print("1. Datenbank laden")
        print("2. Datenbank speichern")
        print("3. Person hinzufügen")
        print("4. Person suchen")
        print("5. Datenbank leeren")
        print("6. Beenden")
        print("\n")

        auswahl = int(input("Auswahl: (1-6) "))
        if auswahl == 1:
            dateiname = input("Bitte kompletten Dateinamen zum Laden eingeben:")
            datei = open(dateiname, "r", encoding="utf-8")
            datenbank.lade(datei)
            datei.close()
            print(f"Datei in Datenbank geladen.")

        elif auswahl == 2:
            dateiname = input("Bitte kompletten Dateinamen zum Speichern eingeben:")
            datei = open(dateiname, "w", encoding="utf-8")
            datenbank.speichere(datei)
            datei.close()
            print("Datenbank in Datei gespeichert.")

        elif auswahl == 3:
            eingabe = input("Bitte Vorname, Nachname und Geburtsdatum im Format 'Vorname, Nachname, JJJJ-MM-TT' eingeben:").split(", ")
            neuePerson = Person(eingabe[0], eingabe[1], eingabe[2])
            datenbank.einfuegen(neuePerson)
            print(f"{neuePerson} eingefügt.")
        
        elif auswahl == 4:
            eingabe = input("Bitte Vorname und Nachname im Format 'Vorname, Nachname' eingeben:").split(", ")
            person = datenbank.findePerson(eingabe[0], eingabe[1])
            if person: print(f"Gefundene Person: {person}")
            else: print(f"Keine Person mit dem Namen {eingabe[0]} {eingabe[1]} gefunden.")
        
        elif auswahl == 5:
            datenbank.leeren()
            print("Datenbank geleert.")

        elif auswahl == 6: break
        else: print("Bitte valide Eingabe machen (1-6).")