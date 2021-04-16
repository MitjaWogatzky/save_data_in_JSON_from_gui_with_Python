"""
In diesem Modul können Skier instanziert werden.
"""

from Archiv.Kl_KindK_Ski_Carver import *
from Archiv.Kl_Kind_Ski_Tourenski import *

# Carver
"""
Notwendige Eigenschaften in entsprechender Reihenfolge: Marke, EK-Preis, Länge in cm, Modelname, Carver-Typ.
Mögliche Carver-Typen: Allround-Carver, Slalom-Carver, Race-Carver, Freeride-Carver.
"""
new_carver = CarverClass("Voelkl", 189.90, 166, "Racetiger SC", "Race Carver")
new_carver.new_carver_json()


# Tourenski
"""
Notwendige Eigenschaften in entsprechender Reihenfolge: Marke, EK-Preis, Länge in cm, Modelname, Carver-Typ.
Mögliche Tourenski-Typen: Abfahrtsorientiert, Generalist, Aufstiegsorientiert.
"""
new_touring_ski = TouringSkiClass("Dynafit", 399.99, 166, "Blacklight Pro", "Aufstiegsorientiert")
new_touring_ski.new_touring_ski_json()
