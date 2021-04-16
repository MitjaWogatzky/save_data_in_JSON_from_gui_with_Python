import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import json
import cartopy.crs as ccrs

# https://openavalancheproject.org/#
#
# def data_US_avalanche_Report() -> list:
#     """Erstellt vier Listen: Longitude, Latitude, Name (der Region), Anzahl
#     (der Lawinen je Region. Gibt die beiden Listen Longitude und Latitude
#     über return zurück"""

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

# print(len(names))
# print(len(amounts))
# print(len(lons))
# print(len(lats))
# print(f"names: {names[0:5]}.")
# print(f"amount: {amounts[0:5]}.")
# print(f"lons: {lons[0:5]}.")
# print(f"lats: {lats[0:5]}.")

ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()
ax.coastlines()

scatter = ax.scatter(lons, lats, color="deepskyblue", s=20, alpha=1.0, label="Lawinenabhänge\nhttps://openavalancheproject.org/#", edgecolors="dodgerblue")

ax.set_xlim(-170, 10)
ax.set_ylim(-20, 90)
ax.legend()

mng = plt.get_current_fig_manager()
mng.window.showMaximized()

plt.show()
