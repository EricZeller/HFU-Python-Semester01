"""Eigenes Modul für Aufgabe 6 mit den Vektorenrechnungen"""

def vektor_summe(a, b):
    """Berechnet die Vektorsumme"""
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return tuple(result)


def skalar_produkt(a, b):
    """Berechnet das Skalarprodukt, also die Summe der paarweisen Produkte der Elemente"""
    x = 0
    result = []
    for i in range(len(a)):
        result.append(a[i] * b[i])
    for i in result:
        x = i + x
    return x


def skaliere(k, a):
    """Der Vektor wird um den Faktor k skaliert, indem seine Elemente mit k multipliziert werden"""
    result = []
    for i in range(len(a)):
        result.append(k * a[i])
    return tuple(result)

