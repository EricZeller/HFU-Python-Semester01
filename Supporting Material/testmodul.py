"""Testmodul für Vorlesung Programmierung"""

def fakultät(n):
    """Berechne die Fakultät einer positiven Ganzzahl"""
    if n <= 1:
        return 1
    else:
        return fakultät(n-1)*n
