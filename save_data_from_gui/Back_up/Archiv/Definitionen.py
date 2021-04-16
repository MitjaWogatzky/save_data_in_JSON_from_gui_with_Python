"""Dieses Modul enthält sämtliche Funktionen, die keiner Klasse oder einem anderen
Modul zugeordnet sind."""

import json


# A) FUNKTIONEN IN ANWENDUNG

# Dateien anlegen und importieren
def dict_ski():
    """Erstellt ein Dictionairy mit unterschiedlichen Typen von Skiern"""
    ski = {"Carver": [], "Tourenski": [], "Allmountain": [], "Freestyle-Ski": []}
    return ski


def renew_ski_json():
    """Leert Datei "ski.json" und legt diese komplett neu an."""
    filename_json = "../ski.json"
    with open(filename_json, "w") as f_json:
        json.dump(dict_ski(), f_json)



def import_json_file() -> dict:
    """Importiert die Datei "ski.json" und übergibt sie als dictionairy"""
    filename = "../ski.json"
    with open(filename, "r") as f:
        contents = json.load(f)
        return contents


# B) DEFINITIONEN, DIE ANGELEGT WURDEN, ABER NICHT IN ANWENDUNG SIND

# Dateien anlegen
def new_ski_json(titel):
    """Erstellt eine völlig neue json-Datei mit "titel als Titel der Datei"""
    filename_json_new = f"{titel}.json"
    with open(filename_json_new, "w") as f_json:
        json.dump(dict_ski(), f_json)


def renew_ski_txt():
    """Leert Datei "ski.txt" und legt diese komplett neu an"""
    filename_txt = f"ski.txt"
    with open(filename_txt, "w") as f_txt:
        f_txt.write(str(dict_ski()))


def new_ski_txt(titel):
    """Erstellt eine völlig neue Textdatei mit "titel als Titel der Datei"""
    filename_txt_new = f"{titel}.txt"
    with open(filename_txt_new, "w") as f_txt:
        f_txt.write(str(dict_ski()))


# Carver und Tourenski auswählen
def select_carver() -> list:
    """Wählt aus der Datei "ski.json" das Schlüssel Werte Paar mit dem
    Schlüsselwort "Carver" aus."""
    f = import_json_file()
    for key, value in f.items():
        if key == "Carver":
            return value


def select_touring() -> list:
    """Wählt aus der Datei "ski.json" das Schlüssel Werte Paar mit dem
    Schlüsselwort "Tourenski" aus."""
    f = import_json_file()
    for key, value in f.items():
        if key == "Tourenski":
            return value


# Listen aus der json-Datei "US-avalanche_report erstellen

def data_us_avalanche_lons() :
    """Erstellt vier Listen: Longitude, Latitude, Name (der Region), Anzahl
    (der Lawinen je Region. Gibt die beiden Listen Longitude und Latitude
    über return zurück"""

    filename = "../US_avalanche_report"

    with open(filename) as f:
        US_avalanche_report = json.load(f)
    avalanches = US_avalanche_report["features"]

    # print(type(US_avalanche_report))
    # print(US_avalanche_report.keys())
    # print(len(US_avalanche_report["features"]))

    names, amounts = [], []

    for avalanche in avalanches:  # erstellt Liste "names"
        name = avalanche["properties"]["name"]
        names.append(name)

    for avalanche in avalanches:  # erstellt Liste "amount" -> je avalanche(Region)
        for key_0, value_0 in avalanche.items():
            if key_0 == "geometry":
                for key_1, value_1 in value_0.items():
                    if key_1 == "coordinates":
                        amount = len(value_1[0])
                        amounts.append(amount)

    print(len(names))
    print(len(amounts))
    print(f"names: {names[0:5]}.")
    print(f"amount: {amounts[0:5]}.")

data_us_avalanche_lons()