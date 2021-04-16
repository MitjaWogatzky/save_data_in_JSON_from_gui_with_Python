"""
Dieses Modul enthält die Kindklasse "Tourenski" samt dazugehörigere Methoden.
Die Elternklasse von "Tourenski" ist "Ski".
"""

from Archiv.Kl_ElternK_Ski import Ski
import json


class TouringSkiClass(Ski):
    """Repräsentiert Aspekte eines Skis, spezifisch von Tourenski"""

    def __init__(self, brand="", purchase_price=float, length=int, name="", typ=""):
        """Initialisieren der Attribute der Elternklasse"""
        super().__init__(brand, purchase_price, length)
        self.name_touring_ski = name
        self.typ = typ

    def describe_touren_ski(self) -> str:
        """Beschreibt die Eigenschaften des Tourenskis"""
        description = f"Model: {self.name_touring_ski}, Klasse: Tourenski, Marke: {self.brand}, " \
                      f"Tourenski-Typ: {self.typ}, Länge: {self.length} cm."
        return description

    def new_touren_ski(self) -> dict:
        """Erstellt ein Dictionary. Basis ist der return Wert (Dictionary) der Methode "new_ski()"
         der Elternklasse "Ski". Dem Dictonairy wird das Schlüssel-Werte Paar "Model" - "Name" hinzugefügt,
         sowie dem Schlüssel-Werte Paar "descritpion" - Dictionary das Schlüssel-Werte Paar
         "typ" und "Ski-Typ"."""
        new_touring_ski = self.new_ski()
        new_touring_ski["model"] = self.name_touring_ski
        for key, value in new_touring_ski.items():
            if key == "description":
                value["typ"] = self.typ
        return new_touring_ski

    def new_touring_ski_json(self):
        """Nimmt das Dictionary des neuen Carver aus def new_carver_description_stock und
        hängt dieses dem Schlüssel "Carver" in der JSON-Datei "ski.json" an."""
        filename_carver = "../ski.json"
        with open(filename_carver, "r") as fc:
            contents = json.load(fc)
            new_contents = {}
            for key, value in contents.items():
                if key == "Tourenski":
                    value.append(self.new_touren_ski())
                new_contents[key] = value
        with open(filename_carver, "w") as fc:
            json.dump(new_contents, fc)
        print(f'Es wurde folgender Tourenski der JSON-Datei "ski.json" hinzugefügt:\n'
              f'{self.describe_touren_ski()}')


if __name__ == "__main__":
    """Zum testen der def new_carver_json"""
    example = TouringSkiClass("dps", 999.99, 163, "Pagoda 106", "Abfahrsorientiert")
    example.new_touring_ski_json()
