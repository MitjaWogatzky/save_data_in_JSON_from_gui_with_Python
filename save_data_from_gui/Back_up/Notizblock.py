# Speichert Veränderung Lagerbestand
def save_stock_carver():
    """Liest Werte des Buttons speicherns (b_stock_carver_save) ein und setzt Variablen add und use."""
    typ_stock = "Carver"
    model_stock = enVar_carver_model_stock.get()  # Erhalten der Eingabewerte.
    length_stock = enVar_carv_length_stock.get()
    try:
        length_stock = int(length_stock)
        # length_stock <= 200
    except ValueError:
        messagebox.showwarning("Fehler Längeneingabe", "Bitte geben Sie bei Länge eine ganze Zahl ein.")

    amount_stock = int(enVar_carv_amount_stock.get())
    option_stock = omVar_stock_carver_option.get()

    add = 0
    use = 0
    if option_stock == stock_carver_option[0]:  # Setzt Variablen gemäße Auswahl.
        add = 1
    if option_stock == stock_carver_option[2]:
        use = 1

    change_amount(typ_stock, model_stock, length_stock, amount_stock, add, use)  #

    enVar_carver_model_stock.set("")  # "Bereinigen" der Eingabefelder.
    enVar_carv_length_stock.set("")
    enVar_carv_amount_stock.set("")
    omVar_stock_carver_option.set(stock_carver_option[3])