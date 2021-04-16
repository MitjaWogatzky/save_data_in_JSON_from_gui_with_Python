"""Enthält alle Funktionen und Funtkionsaufrufe zum Thema "Lagerhaltung"."""

import json
from Archiv import Definitionen as Def


def change_amount(typ="".upper(), model="".upper(), length=int, amount=int, add=bool, use=bool):
    """Erhöht Lagerbestand der Typ-, Model-, Längenkombination um amount"""
    new_contents = {}
    current_length = 0
    current_stock = 0
    f = Def.import_json_file()
    filename = "../ski.json"
    for key, value in f.items():
        if key == typ:
            for ski in value:
                for key_ski, value_i in ski.items():
                    if key_ski == "description":
                        current_length = value_i["length"]
                    if key_ski == "stock":
                        current_stock = value_i
                    if key_ski == "model" and value_i == model:
                        if current_length == length:
                            if use:
                                current_stock = amount
                            else:
                                if add:
                                    current_stock += amount
                                else:
                                    current_stock -= amount
                            # print(model, current_length, current_stock)
                            ski["stock"] = current_stock
                            new_contents[key] = value
                            print(f"Der neue Lagerebestand des Ski's {model} ist {current_stock}.")
        else:
            new_contents[key] = value
    with open(filename, "w") as fc:
        json.dump(new_contents, fc)


if __name__ == "__main__":
    # Ski hinzufügen
    print(change_amount("Tourenski", "Blacklight Pro", 166, 50, 1, 0))
    # Ski herausnehmen
    print(change_amount("Tourenski", "Blacklight Pro", 166, 20, 0, 0))
    # Lagerbestand neu setzen
    print(change_amount("Tourenski", "Blacklight Pro", 166, 5, 0, 1))


