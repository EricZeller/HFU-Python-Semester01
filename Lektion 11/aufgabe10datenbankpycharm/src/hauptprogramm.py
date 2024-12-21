from personendatenbank import Person
from personendatenbank import Personendatenbank

def mainloop():
    datenbank = Personendatenbank()
    while True:
        print("\nWähle eine Option:")
        print("1. Datenbank laden")
        print("2. Datenbank speichern")
        print("3. Person hinzufügen")
        print("4. Person suchen")
        print("5. Datenbank leeren")
        print("6. Kommende Geburtstage anzeigen")
        print("7. Beenden")
        print("\n")

        auswahl = int(input("Auswahl: (1-7) "))
        if auswahl == 1:
            dateiname = "./" + input("Bitte kompletten Dateinamen zum Laden eingeben: ")
            if not dateiname.endswith(".json"): dateiname = dateiname + ".json"
            datei = open(dateiname, "r", encoding="utf-8")
            datenbank.lade(datei)
            datei.close()
            print(f"Datei in Datenbank geladen.")

        elif auswahl == 2:
            dateiname = "./" + input("Bitte kompletten Dateinamen zum Speichern eingeben: ")
            if not dateiname.endswith(".json"): dateiname = dateiname + ".json"
            datei = open(dateiname, "w", encoding="utf-8")
            datenbank.speichere(datei)
            datei.close()
            print("Datenbank in Datei gespeichert.")

        elif auswahl == 3:
            eingabe = input(
                "Bitte Vorname, Nachname und Geburtsdatum im Format 'Vorname, Nachname, JJJJ-MM-TT' eingeben: ").split(
                ", ")
            neuePerson = Person(eingabe[0], eingabe[1], eingabe[2])
            datenbank.einfuegen(neuePerson)
            print(f"{neuePerson} eingefügt.")

        elif auswahl == 4:
            eingabe = input("Bitte Vorname und Nachname im Format 'Vorname, Nachname' eingeben: ").split(", ")
            person = datenbank.findePerson(eingabe[0], eingabe[1])
            if person:
                print(f"Gefundene Person: {person}")
            else:
                print(f"Keine Person mit dem Namen {eingabe[0]} {eingabe[1]} gefunden.")

        elif auswahl == 5:
            datenbank.leeren()
            print("Datenbank geleert.")

        elif auswahl == 6:
            i = 0
            print("Die Personen, die als nächstes Geburtstag haben sind: ")
            for p in datenbank.naechste_geburtstage():
                nAlter = p.naechster_geburtstag().year - p.bday.year
                print(f"- {p.fname} {p.lname}, feiert am {p.naechster_geburtstag()} den {nAlter}. Geburtstag")
                i += 1
                if i == 5: break

        elif auswahl == 7:
            print("Auf Wiedersehen!")
            break
        else:
            print("Bitte valide Eingabe machen (1-6).")