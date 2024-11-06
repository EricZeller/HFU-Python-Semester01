"""Zweites Testmodul für die Vorlesung Programmieren"""

def ggt(a,b):
    """Berechne den größten gemeinsamen Teiler zweier positiver Ganzzahlen"""
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print("Dieser Code wird beim Import ausgeführt!")
