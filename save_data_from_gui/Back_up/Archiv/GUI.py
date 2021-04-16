from tkinter import *
import tkinter.ttk as ttk
from Archiv import Kl_KindK_Ski_Carver as klca, Lagerhaltung as La
import matplotlib.pyplot as plt
import json
import cartopy.crs as ccrs
from tkinter import messagebox


def save_new_carver():
    """Erstellt aus den Eingabe des Labelframes "Neuer Carver einen neuen
    Eintrag in der Datei "ski.json"""

    brand = omVar_new_carver_brand.get()
    price = float(enVar_carv_price.get())
    length = int(enVar_carv_length.get())
    model = en_new_carver_model.get()
    typ = omVar_new_carver_typ.get()



    omVar_new_carver_brand.set(carver_brandlist[8])
    enVar_carv_price.set("")
    enVar_carv_length.set("")
    enVar_carv_model.set("")
    omVar_new_carver_typ.set(carver_typ[4])

    new_carver = klca.CarverClass(brand, price, length, model, typ)
    new_carver.new_carver_json()


def save_stock_carver():
    """Ändert den Bestand des angegebenen Skis in der Datei "ski.json."""
    typ_stock = "Carver"
    model_stock = enVar_carver_model_stock.get()
    length_stock = int(enVar_carv_length_stock.get())
    amount_stock = int(enVar_carv_amount_stock.get())
    option_stock = omVar_stock_carver_option.get()
    add = 0
    use = 0
    if option_stock == stock_carver_option[0]:
        add = 1
    if option_stock == stock_carver_option[2]:
        use = 1

    change_stock = La.change_amount(typ_stock, model_stock, length_stock, amount_stock, add, use)

    enVar_carver_model_stock.set("")
    enVar_carv_length_stock.set("")
    enVar_carv_amount_stock.set("")
    omVar_stock_carver_option.set(stock_carver_option[3])


# Anlegen von dict mit Ski-Typen
def dict_ski() -> dict:
    """Erstellt ein Dictionairy mit unterschiedlichen Typen von Skiern"""
    ski = {"Carver": [], "Tourenski": [], "Allmountain": [], "Freestyle-Ski": []}
    return ski


# Erstellen json-Datei mit Ski-Typen
def new_ski_json():
    """Erstellt neue json-Datei "ski.json bzw. leert vorhanden Datei."""
    filename_json = "../ski.json"
    with open(filename_json, "w") as f_json:            # Erstellen der Datei mit der Liste aus dict_ski().
        json.dump(dict_ski(), f_json)


def data_US_avalanche_Report():
    """Erstellt zwei Listen: lons, lats.
    Lons: Longituden
    Lats: Latituden
    Basis: json Datei, Quelle: https://openavalancheproject.org/#
    Datei: https://raw.githubusercontent.com/scottcha/OpenAvalancheProject/master/Data/USAvalancheRegions.geojson
    """
    filename = "../US_avalanche_report"

    with open(filename) as f:
        US_avalanche_report = json.load(f)
    avalanches = US_avalanche_report["features"]

    # print(type(US_avalanche_report))
    # print(US_avalanche_report.keys())
    # print(len(US_avalanche_report["features"]))

    lons, lats = [], []

    for avalanche in avalanches:  # erstellt Liste "lons" und "lats"
        for key_1, value_1 in avalanche.items():
            if key_1 == "geometry":
                for key_2, value_2 in value_1.items():
                    if key_2 == "coordinates":
                        val2 = value_2[0]
                        for i in val2:
                            if isinstance(i[0], float) and isinstance(i[1], float):
                                lon = i[0]
                                lat = i[1]
                                lons.append(lon)
                                lats.append(lat)

    return lons, lats


def show_avalanche_map():
    """Erstellt eine Graphik der Lawinenabgänge in den USA.
    Daten erhält Funtkion aus data_US_avalanche_Report()"""

    lons, lats = data_US_avalanche_Report()

    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.stock_img()
    ax.coastlines()

    scatter = ax.scatter(lons, lats, color="deepskyblue", s=20, alpha=1.0,
                         label="Lawinenabhänge, März 2020\nhttps://openavalancheproject.org/#",
                         edgecolors="dodgerblue")

    ax.set_xlim(-170, 10)
    ax.set_ylim(-20, 90)
    ax.legend()

    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()

    plt.show()


root = Tk()
root.geometry = "900x900"
f = Frame(root, width=500, height=100)
f.grid()

# ÜBERSCHRIFT
l1 = Label(f, text="Ski Verwaltung", font=("default", "20"), pady=20)
l1.grid(row=0, column=0, columnspan=1)


# NOTEBOOK ANLEGEN
nb = ttk.Notebook(f, width=324, height=600)
tab_admin_carver = ttk.Frame(nb)
tab_admin_touring = ttk.Frame(nb)
tab_admin_all_mountain = ttk.Frame(nb)
tab_admin_freestyle = ttk.Frame(nb)
tab_admin_misc = ttk.Frame(nb)
nb.add(tab_admin_carver, text ="Carver")
nb.add(tab_admin_touring, text="Tourenski")
nb.add(tab_admin_all_mountain, text= "All-Mountain")
nb.add(tab_admin_freestyle, text= "Freestyle")
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

# speichern Neuer Carver
b_new_carver_save = Button(lf_new_carver, text="speichern", command=save_new_carver)
b_new_carver_save.grid(row=7, columnspan=3, pady=20, padx=4)


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

# messagebox Feedback neuer Carver

res = messagebox.showinfo(klca.newnew_carver_json)
print(res,type(res))

root.title('Skiverleih Python')
root.mainloop()
