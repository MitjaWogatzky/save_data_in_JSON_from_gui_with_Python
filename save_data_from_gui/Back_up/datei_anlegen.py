import json

def dict_ski() -> dict:
    """Erstellt ein Dictionairy mit unterschiedlichen Typen von Skiern"""
    ski = {"Carver": [], "Tourenski": [], "Allmountain": [], "Freestyle-Ski": []}
    return ski


# Erstellen json-Datei mit Ski-Typen
def new_ski_json():
    """Erstellt neue json-Datei "ski.json bzw. leert vorhanden Datei."""
    filename_json = "ski.json"
    with open(filename_json, "w") as f_json:  # Erstellen der Datei mit der Liste aus dict_ski().
        json.dump(dict_ski(), f_json)

new_ski_json()
