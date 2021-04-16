"""Dieses Programm stellt die Lagerhaltung für einen Skiverleih dar.
Am Beispiel von Carvern können neue Skimodell gespeichert und deren Bstand verändert werden.
Zudem werden können Lawinenabgänge in den USA im Frühjahr 2020 angezeigt werden"""


# IMPORTS
import json
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import tkinter.ttk as ttk
import cartopy.crs as ccrs


# KLASSEN

# Elternklasse "Ski"
class Ski:
    """Eine einfache Beschreibung eines Skiers. Elternklasse "Ski" enthält die Kindklassen:
    "Carver", "Tourenski", "Allmountain", "Freestyle-Ski"."""

    # Initialieren der Attribute
    def __init__(self, brand="", purchase_price=float, length=int):
        """Initialisieren von Atrributen, die Ski beschreiben."""
        self.brand = brand
        self.purchase_price = purchase_price
        self.length = length

    # Erstellen eines neuen Ski mit Attributen Elternklasse
    def new_ski(self) -> dict:
        """Erstellt ein Dictionary. Inhalt:
        a) "description": Dictionary, welches Attribute des Skis enthält
        b) "stock": Lager-Anfangsbestand mit int-Wert 0.
        Der Ski benötigt noch weitere Angaben, je nach Ski-Typ"""
        new_ski, description, stock = {}, {}, {}                # anlegen leerer Dictionairies
        description["brand"] = self.brand                       # füllen des dictionairies "description" mit
        description["purchase_price"] = self.purchase_price     # den Attributen "Brand", "Purchase_Price" und "length"
        description["length"] = self.length
        new_ski["description"] = description                    # anhängen dict "description" an dict "new_ski"
        new_ski["stock"] = 0                                    # anhängen Sch_W-Paar "Stock" an dict "new_ski"
        return new_ski


# Kindklasse "Carver"
class Carver(Ski):
    """Repräsentiert Aspekte eines Skis, spezifisch von Carvern"""

    # Initialieren der Attribute
    def __init__(self, brand="", purchase_price=float, length=int, name="", typ=""):
        """Initialisieren der Attribute der Elternklasse"""
        super().__init__(brand, purchase_price, length)
        self.name_carver = name
        self.typ = typ

    # Beschreibung Carver
    def describe_carver(self) -> str:
        """Beschreibt die Eigenschaften des Carvers"""
        description = f"Model: {self.name_carver}\n" \
                      f"Klasse: Caver\n" \
                      f"Marke: {self.brand}\n" \
                      f"Carver-Typ: {self.typ}\n" \
                      f"Länge: {self.length} cm."
        return description

    # Erstellung eines neuen Carvers
    def new_carver(self) -> dict:
        """Erweitert das dict aus new_ski(), welches die Attribute der Elternklasse enthält
        Inhalt:
        a) Weiteres Sch-W-Paar: "model" mit Modelname
        b) Carvertyp wird in description eingefügt."""
        new_carver = self.new_ski()             # Erhalt der Attribute eines Skis (Elternklasse) als dict.
        new_carver["model"] = self.name_carver  # anhängen dict Sch-W-Paar "Model" "new_carver"
        for key, value in new_carver.items():   # anhängen Sch-W-Paar "typ" an dict "description"
            if key == "description":
                value["typ"] = self.typ
        return new_carver

    # Einfügen des neuen Carvers in die json-Datei
    def new_carver_json(self):
        """Nimmt das dict aus new_carver() und fügt es dem Schlüssel "Carver" in der json-Datei "ski.json" an."""
        filename_carver = "../../Abschlussprojekt_Wogatzky/ski.json"
        with open(filename_carver, "r") as fc:          # öffnen und laden der json-Datei.
            contents = json.load(fc)
            new_contents = {}                           # neues dict zur Überschreibung der json-Datei
            for key, value in contents.items():         # einfügen des des dict aus new_carver() an json-Datei
                if key == "Carver":                     # unter Schlüssel "Carver"
                    value.append(self.new_carver())
                new_contents[key] = value               # Speichern der Werte in neuem dict.
        with open(filename_carver, "w") as fc:          # Überschreiben der json-Datei mit den neuen Werten
            json.dump(new_contents, fc)
        print(f'Es wurde folgender Carver der JSON-Datei "ski.json" hinzugefügt:\n' 
              f'{self.describe_carver()}')              # Info-Zeile, welcher Carver hinzugefügt wurde.


# Kindklasse "Tourenski"
class TouringSki(Ski):
    """Repräsentiert Aspekte eines Skis, spezifisch von Tourenski"""

    # Initialieren der Attribute
    def __init__(self, brand="", purchase_price=float, length=int, name="", typ=""):
        """Initialisieren der Attribute der Elternklasse"""
        super().__init__(brand, purchase_price, length)
        self.name_touring_ski = name
        self.typ = typ

    # Beschreibung Tourenski
    def describe_touren_ski(self) -> str:
        """Beschreibt die Eigenschaften des Tourenskis"""
        description = f"Model: {self.name_touring_ski}, Klasse: Tourenski, Marke: {self.brand}, " \
                      f"Tourenski-Typ: {self.typ}, Länge: {self.length} cm."
        return description

    # Erstelung eines neuen Tourenskis
    def new_touren_ski(self) -> dict:
        """Erweitert das dict aus new_ski(), welches die Attribute der Elternklasse enthält
        Inhalt:
        a) Weiteres Sch-W-Paar: "model" mit Modelname
        b) Tourenski-typ wird in description eingefügt."""
        new_touring_ski = self.new_ski()                    # Erhalt der Attribute eines Skis (Elternklasse) als dict.
        new_touring_ski["model"] = self.name_touring_ski    # anhängen dict Sch-W-Paar "Model" "new_touring_ski"
        for key, value in new_touring_ski.items():          # anhängen Sch-W-Paar "typ" an dict "description"
            if key == "description":
                value["typ"] = self.typ
        return new_touring_ski

    # Einfügen des neuen Tourenskis in die json-Datei
    def new_touring_ski_json(self):
        """Nimmt das dict aus new_touren_ski() und fügt es dem Schlüssel "Tourenski" in der json-Datei "ski.json" an."""
        filename_carver = "../../Abschlussprojekt_Wogatzky/ski.json"
        with open(filename_carver, "r") as fc:          # öffnen und laden der json-Datei.
            contents = json.load(fc)
            new_contents = {}                           # neues dict zur Überschreibung der json-Datei
            for key, value in contents.items():         # einfügen des dict aus new_touren_ski() an json-Datei
                if key == "Tourenski":                  # unter Schlüssel "Tourenski"
                    value.append(self.new_touren_ski())
                new_contents[key] = value               # Speichern der Werte in neuem dict.
        with open(filename_carver, "w") as fc:          # Überschreiben der json-Datei mit den neuen Werten
            json.dump(new_contents, fc)
        print(f'Es wurde folgender Tourenski der JSON-Datei "ski.json" hinzugefügt:\n'
              f'{self.describe_touren_ski()}')          # Info-Zeile, welcher Tourenski hinzugefügt wurde.


# DATEIVERWALTUNG

# Anlegen von dict mit Ski-Typen
def dict_ski() -> dict:
    """Erstellt ein Dictionairy mit unterschiedlichen Typen von Skiern"""
    ski = {"Carver": [], "Tourenski": [], "Allmountain": [], "Freestyle-Ski": []}
    return ski


# Erstellen json-Datei mit Ski-Typen
def new_ski_json():
    """Erstellt neue json-Datei "ski.json bzw. leert vorhanden Datei."""
    filename_json = "../../Abschlussprojekt_Wogatzky/ski.json"
    with open(filename_json, "w") as f_json:            # Erstellen der Datei mit der Liste aus dict_ski().
        json.dump(dict_ski(), f_json)


# Importiert json-Datei für dict
def import_json_file() -> dict:
    """Importiert die Datei "ski.json" und übergibt sie als dictionairy"""
    filename = "../../Abschlussprojekt_Wogatzky/ski.json"
    with open(filename, "r") as f_json:                 # Importiert Datei "ski.json" und erstellt ein dict aus ihr.
        contents = json.load(f_json)
        return contents


# MATPLOTLIB LAWINENGRAPHIK

# Erstellen von Listen zu Ortsangaben vON Lawinenabgängen
def data_us_avalanche_report():
    """Erstellt zwei Listen (lons, lats), um Ortsangaben zu Lawinenabgängen verwenden zu können.
    Lons: Longituden
    Lats: Latituden
    Basis: json Datei, Quelle: https://openavalancheproject.org/#
    Rohdaten: https://raw.githubusercontent.com/scottcha/OpenAvalancheProject/master/Data/USAvalancheRegions.geojson
    """
    filename = "us_avalanche_report"

    with open(filename) as f:                           # Öffnen und laden der Rohdaten
        us_avalanche_report = json.load(f)
    avalanches = us_avalanche_report["features"]        # Auswahl des Sch-W-Paars "features"

    lons, lats = [], []                                 # Listen für Graphik

    for avalanche in avalanches:                        # Liste der Regionen mit erfassten Lawinen öffnen
        for key_1, value_1 in avalanche.items():
            if key_1 == "geometry":
                for key_2, value_2 in value_1.items():
                    if key_2 == "coordinates":
                        val2 = value_2[0]               # Liste mit Ortsangaben je Lawinenregion öffnen
                        for i in val2:
                            if isinstance(i[0], float) and isinstance(i[1], float):
                                lon = i[0]              # Prüfung ob Eintrag eine Float-Variable ist,
                                lat = i[1]              # aufgrund inhomogener Daten
                                lons.append(lon)        # Befüllen der Liste "lons"
                                lats.append(lat)        # Befüllen der Liste "lats"

    return lons, lats


# Erstellen einer matplotlib Graphik von Lawinenabgängen in den USA
def show_avalanche_map():
    """Erstellt eine Graphik der Lawinenabgänge in den USA.
    Daten erhält Funtkion aus data_US_avalanche_Report()"""

    lons, lats = data_us_avalanche_report()             # Erhalten der Listen mit Longituden und Latituden

    ax = plt.axes(projection=ccrs.PlateCarree())        # Laden der Landkarte von PlateCarree
    ax.stock_img()
    ax.coastlines()
    ax.scatter(lons, lats, color="deepskyblue", s=20, alpha=1.0,
                label="Lawinenabhänge, März 2020\nhttps://openavalancheproject.org/#",
                edgecolors="dodgerblue")
    ax.set_xlim(-170, 10)
    ax.set_ylim(-20, 90)
    ax.legend()

    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()

    plt.show()


# GUI

# Speichert eingegebenen Carver
def save_new_carver():
    """Erstellt aus den Eingabe des Labelframes "Neuer Carver einen neuen
    Eintrag in der Datei "ski.json"""

    brand = omVar_new_carver_brand.get()                # Erhalten der Eingabewerte
    price = float(enVar_carv_price.get())
    length = int(enVar_carv_length.get())
    model = en_new_carver_model.get()
    typ = omVar_new_carver_typ.get()

    omVar_new_carver_brand.set(carver_brandlist[8])     # "Bereinigen" der Eingabefelder
    enVar_carv_price.set("")
    enVar_carv_length.set("")
    enVar_carv_model.set("")
    omVar_new_carver_typ.set(carver_typ[4])

    new_carver = Carver(brand, price, length, model, typ)   # Einspeisen der Eingabewerte in Funktion zum anlegen
    new_carver.new_carver_json()                            # eines neuen Carvers nud speichern in Datei "ski.json"

    messagebox.showinfo("Neuer Ski", f'Es wurde folgender Carver dem Bestand hinzugefügt:\n\n'
                         f'{Carver.describe_carver(new_carver)}')


# ändert den Lagerbestand
def change_amount(typ="".upper(), model="".upper(), length=int, amount=int, add=bool, use=bool):
    """Erhöht Lagerbestand der Typ-, Model-, Längenkombination um amount"""
    new_contents = {}                                       # Anlegen eines dict zum Überschreiben der alten Werte
    current_length = 0                                      # Variablen zum Abgleich der Eingabewerte mit
    current_stock = 0                                       # Werten aus json Datei
    f = import_json_file()
    filename = "../../Abschlussprojekt_Wogatzky/ski.json"
    for key, value in f.items():                            # Skityp identifizieren
        if key == typ:                                      # Prüfung Skityp
            for ski in value:                               # Sepzifisches Model und Länge identifizieren
                for key_ski, value_i in ski.items():
                    if key_ski == "description":
                        current_length = value_i["length"]  # übernimmt abgespeicherten Wert Länge
                    if key_ski == "stock":
                        current_stock = value_i             # übernahme abgespeicherter Wert
                    if key_ski == "model" and value_i == model:
                        if current_length == length:        # Art der Mengenänderung bestimmen
                            if use:
                                current_stock = amount
                            else:
                                if add:
                                    current_stock += amount
                                else:
                                    current_stock -= amount
                            ski["stock"] = current_stock    # Neuen Bestandswert übergeben
                            new_contents[key] = value       # Alten Wert in neues dict eintragen
                            # print(f"Der neue Lagerebestand des Ski's {model} ist {current_stock}.")
                            messagebox.showinfo("Änderung Lagerbestand", f'Der neue Lagerebestand des Ski "{model}"\n'
                                               f' mit der Länge {current_length} ist {current_stock}.')
        else:
            new_contents[key] = value                       # neues dict mit bisherigen, ungeänderten Werten füllen
    with open(filename, "w") as fc:
        json.dump(new_contents, fc)                         # neues dict in Datei "ski.json" schreiben



# Speichert Veränderung Lagerbestand
def save_stock_carver():
    """Liest Werte des Buttons speicherns (b_stock_carver_save) ein und setzt Variablen add und use."""
    typ_stock = "Carver"
    model_stock = enVar_carver_model_stock.get()            # Erhalten der Eingabewerte
    length_stock = int(enVar_carv_length_stock.get())
    amount_stock = int(enVar_carv_amount_stock.get())
    option_stock = omVar_stock_carver_option.get()
    add = 0
    use = 0
    if option_stock == stock_carver_option[0]:              # Setzt Variablen gemäße Auswahl
        add = 1
    if option_stock == stock_carver_option[2]:
        use = 1

    change_amount(typ_stock, model_stock, length_stock, amount_stock, add, use) #

    enVar_carver_model_stock.set("")                        # "Bereinigen" der Eingabefelder
    enVar_carv_length_stock.set("")
    enVar_carv_amount_stock.set("")
    omVar_stock_carver_option.set(stock_carver_option[3])


# GUI PROGRAMMABLAUF

root = Tk()
root.geometry = "900x900"

# RAHMEN und ÜBERSCHRIFT
f = Frame(root, width=500, height=100)
f.grid()
l1 = Label(f, text="Ski Verwaltung", font=("default", "20"), pady=20)
l1.grid(row=0, column=0, columnspan=1)


# NOTEBOOK ANLEGEN
nb = ttk.Notebook(f, width=324, height=600)
tab_admin_carver = ttk.Frame(nb)
tab_admin_touring = ttk.Frame(nb)
tab_admin_all_mountain = ttk.Frame(nb)
tab_admin_freestyle = ttk.Frame(nb)
tab_admin_misc = ttk.Frame(nb)
nb.add(tab_admin_carver, text="Carver")
nb.add(tab_admin_touring, text="Tourenski")
nb.add(tab_admin_all_mountain, text="All-Mountain")
nb.add(tab_admin_freestyle, text="Freestyle")
nb.add(tab_admin_misc, text="Allgemein")
nb.grid()


# TAB NEUER CARVER

# CARVER ANLEGEN

# Labelframe "Neuer Carver"
lf_new_carver = ttk.LabelFrame(tab_admin_carver, text="Neuer Carver")
lf_new_carver.grid(row=0, column=0, columnspan=3, ipadx=30, padx=8, pady=15, sticky=W)
la_new_carver = ttk.Label(lf_new_carver, text="Hier können Sie einen neuen Carver anlegen.")
la_new_carver.grid(row=1, column=0, columnspan=3, pady=12, padx=4)

# Marke Neuer Carver
omVar_new_carver_brand = StringVar()
carver_brandlist = ["Atomic", "Fischer", "Head", "K2", "Nordica", "Rossignol", "Salomon", "Voelkl", ""]
# carver_brandlist = sorted(carver_brandlist)

la_new_carver_brand = ttk.Label(lf_new_carver, text="Marke:")
la_new_carver_brand.grid(row=2, column=0, pady=2, sticky=W, padx=6)
om_new_carver_brand = OptionMenu(lf_new_carver, omVar_new_carver_brand, *carver_brandlist)
om_new_carver_brand.grid(row=2, column=1, pady=1, sticky=W, padx=4)

# Preis Neuer Carver
enVar_carv_price = StringVar()

la_new_carver_price = ttk.Label(lf_new_carver, text="Preis:")
la_new_carver_price.grid(row=3, column=0, pady=2, sticky=W, padx=6)
en_new_carver_price = ttk.Entry(lf_new_carver, textvariable=enVar_carv_price)
en_new_carver_price.grid(row=3, column=1, pady=1, sticky=W, padx=4)
la_new_carver_price_desc = ttk.Label(lf_new_carver, text="€.CC")
la_new_carver_price_desc.grid(row=3, column=2, pady=2, sticky=W)

# Länge Neuer Carver
enVar_carv_length = StringVar()

la_new_carver_length = ttk.Label(lf_new_carver, text="Länge:")
la_new_carver_length.grid(row=4, column=0, pady=2, sticky=W, padx=6)
en_new_carver_length = ttk.Entry(lf_new_carver, textvariable=enVar_carv_length)
en_new_carver_length.grid(row=4, column=1, pady=1, sticky=W, padx=4)
la_new_carver_length_desc = ttk.Label(lf_new_carver, text="cm")
la_new_carver_length_desc.grid(row=4, column=2, pady=2, sticky=W)

# Model Neuer Carver
enVar_carv_model = StringVar()

la_new_carver_model = ttk.Label(lf_new_carver, text="Model:")
la_new_carver_model.grid(row=5, column=0, pady=2, sticky=W, padx=6)
en_new_carver_model = ttk.Entry(lf_new_carver, textvariable=enVar_carv_model)
en_new_carver_model.grid(row=5, column=1, pady=1, sticky=W, padx=4)

# Typ Neuer Carver
omVar_new_carver_typ = StringVar()
carver_typ = ["Allround", "Freeride",  "Slalom", "Race", ""]

la_new_carver_typ = ttk.Label(lf_new_carver, text="Typ:")
la_new_carver_typ.grid(row=6, column=0, pady=2, sticky=W, padx=6)
om_new_carver_typ = OptionMenu(lf_new_carver, omVar_new_carver_typ, *carver_typ)
om_new_carver_typ.grid(row=6, column=1, pady=1, sticky=W, padx=4)

# speichern neuer Carver
b_new_carver_save = Button(lf_new_carver, text="speichern", command=save_new_carver)
b_new_carver_save.grid(row=7, columnspan=3, pady=20, padx=4)

# Informationsanzeige neuer Carver


# BESTAND ÄNDERN

# Labelframe "Bestand"
lf_new_stock = ttk.LabelFrame(tab_admin_carver, text="Bestandsverwaltung")
lf_new_stock.grid(row=1, column=0, columnspan=2, ipadx=40, padx=8, pady=10)
la_new_stock = ttk.Label(lf_new_stock, text="Hier können Sie den Bestand ändern.\nBitte geben Model und die Länge an.")
la_new_stock.grid(row=0, column=0, columnspan=3, pady=12, padx=4, sticky=W)

# Model Bestand
enVar_carver_model_stock = StringVar()

la_stock_carver_model = ttk.Label(lf_new_stock, text="Model:")
la_stock_carver_model.grid(row=1, column=0, pady=1, sticky=W, padx=6)
en_stock_carver_model = ttk.Entry(lf_new_stock, textvariable=enVar_carver_model_stock)
en_stock_carver_model.grid(row=1, column=1, pady=1, sticky=W, padx=4)

# Länge Bestand
enVar_carv_length_stock = StringVar()

la_stock_carver_length = ttk.Label(lf_new_stock, text="Länge:")
la_stock_carver_length.grid(row=2, column=0, pady=2, sticky=W, padx=6)
en_stock_carver_length = ttk.Entry(lf_new_stock, textvariable=enVar_carv_length_stock)
en_stock_carver_length.grid(row=2, column=1, pady=1, sticky=W, padx=4)
la_stock_carver_length_desc = ttk.Label(lf_new_stock, text="cm")
la_stock_carver_length_desc.grid(row=2, column=2, pady=2, sticky=W)

# Menge Bestand
la_change_stock = ttk.Label(lf_new_stock, text="Mengenänderung:\nMenge und Art der Änderung angeben.")
la_change_stock.grid(row=3, column=0, columnspan=3, pady=8, padx=4, sticky=SW)

enVar_carv_amount_stock = StringVar()
la_stock_carver_amount = ttk.Label(lf_new_stock, text="Menge:")
la_stock_carver_amount.grid(row=4, column=0, pady=2, sticky=W, padx=6)
en_stock_carver_amount = ttk.Entry(lf_new_stock, textvariable=enVar_carv_amount_stock)
en_stock_carver_amount.grid(row=4, column=1, pady=2, sticky=W, padx=4)

# ändern Bestand
omVar_stock_carver_option = StringVar()
stock_carver_option = ["hinzufügen", "entnehmen", "Menge neu setzen", ""]

la_stock_carver_option = ttk.Label(lf_new_stock, text="Änderung:")
la_stock_carver_option.grid(row=5, column=0, pady=2, sticky=W, padx=6)
om_stock_carver_change = OptionMenu(lf_new_stock, omVar_stock_carver_option, *stock_carver_option)
om_stock_carver_change.grid(row=5, column=1, pady=1, sticky=W, padx=4)

# speichern Bestand
b_stock_carver_save = Button(lf_new_stock, text="speichern", command=save_stock_carver)
b_stock_carver_save.grid(row=6, columnspan=3, pady=20, padx=2)


# TAB ALLGEMEIN

# Labelframe "Allgemein"
lf_new_file = ttk.LabelFrame(tab_admin_misc, text="Neue Datei")
lf_new_file.grid(row=0, column=0, columnspan=3, ipadx=63, padx=8, pady=15)
la_new_file = ttk.Label(lf_new_file, text="Hier können Sie eine neue Datei\n"
                                          "zur Skiverwaltung anlegen.")
la_new_file.grid(row=0, column=0, columnspan=3, pady=15, padx=4)

b_new_file = Button(lf_new_file, text="Datei anlegen", command=new_ski_json)
b_new_file.grid(row=1, columnspan=3, pady=20, padx=4, sticky=W)

# Labelframe "Lawinenreport"
lf_avalanche_report = ttk.LabelFrame(tab_admin_misc, text="Lawinenreport")
lf_avalanche_report.grid(row=1, column=0, columnspan=3, ipadx=42, padx=8, pady=15)
la_new_file = ttk.Label(lf_avalanche_report, text="Report zu Lawinenabgängen in den USA\nStand: März 2020")
la_new_file.grid(row=0, column=0, columnspan=3, pady=12, padx=4)

b_avalanche_report = Button(lf_avalanche_report, text="Report anzeigen", command=show_avalanche_map)
b_avalanche_report.grid(row=1, columnspan=3, pady=15, padx=4, sticky=W)

root.title('Pythonski')
root.mainloop()
