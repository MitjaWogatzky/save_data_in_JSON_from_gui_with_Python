"""
Dieses Modul enthält die Elternklasse "Ski" samt dazugehörigere Methoden.
"""

import json


class Ski:
    """Eine einfache Beschreibung eines Skiers.
    Elternklasse "Ski" enthält die Kindklassen:
    "Carver", "Tourenski", "Allmountain", "Freestyle-Ski"."""

    def __init__(self, brand="", purchase_price=float, length=int):
        """Initialisieren von Atrributen, die Ski beschreiben."""
        self.brand = brand
        self.purchase_price = purchase_price
        self.length = length

    def new_ski(self) -> dict:
        """Erstellt ein Dictionary. Diese enthält a) den Schlüssel "description"
        mit einem Dictionary als Wert, welches Attribute des Skis enthält,
        und b) den Schlüssel "stock", welcher den int-Wert 0 enthält."""
        new_ski, description, stock = {}, {}, {}
        description["brand"] = self.brand
        description["purchase_price"] = self.purchase_price
        description["length"] = self.length
        new_ski["description"] = description
        new_ski["stock"] = 0
        return new_ski
