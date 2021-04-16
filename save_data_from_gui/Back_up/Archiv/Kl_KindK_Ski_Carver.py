"""
Dieses Modul enthält die Kindklasse "Carver" samt dazugehörigere Methoden.
Die Elternklasse von "Carver" ist "Ski".
"""

from Archiv.Kl_ElternK_Ski import Ski
import json


class CarverClass(Ski):
    """Repräsentiert Aspekte eines Skis, spezifisch von Carvern"""

    def __init__(self, brand="", purchase_price=float, length=int, name="", typ=""):
        """Initialisieren der Attribute der Elternklasse"""
        super().__init__(brand, purchase_price, length)
        self.name_carver = name
        self.typ = typ

    def describe_carver(self) -> str:
        """Beschreibt die Eigenschaften des Carvers"""
        description = f"Model: {self.name_carver}, Klasse: Caver, Marke: {self.brand}, " \
                      f"Carver-Typ: {self.typ}, Länge: {self.length} cm."
        return description

    def new_carver(self) -> dict:
        """Erstellt ein Dictionary. Basis ist der return Wert (Dictionary) der Methode "new_ski()"
         der Elternklasse "Ski". Dem Dictonairy wird das Schlüssel-Werte Paar "Model" - "Name" hinzugefügt,
         sowie dem Schlüssel-Werte Paar "descritpion" - Dictionary das Schlüssel-Werte Paar
         "typ" und "Ski-Typ"."""
        new_carver = self.new_ski()
        new_carver["model"] = self.name_carver
        for key, value in new_carver.items():
            if key == "description":
                value["typ"] = self.typ
        return new_carver

    def new_carver_json(self):
        """Nimmt das Dictionary des neuen Carver aus def new_carver und hängt dieses dem
        Schlüssel "Carver" in der JSON-Datei "ski.json" an."""
        filename_carver = "../ski.json"
        with open(filename_carver, "r") as fc:
            contents = json.load(fc)
            new_contents = {}
            for key, value in contents.items():
                if key == "Carver":
                    value.append(self.new_carver())
                new_contents[key] = value
        with open(filename_carver, "w") as fc:
            json.dump(new_contents, fc)
        feedback_new_carver = f'Es wurde folgender Carver der JSON-Datei "ski.json" hinzugefügt:\n' \
                              f'{self.describe_carver()}'
        return feedback_new_carver

if __name__ == "__main__":
    """Zum testen der def new_carver_json"""
    example = CarverClass("Atomic", 199.90, 170, "Redster X7", "Race Carver")
    example.new_carver_json()
