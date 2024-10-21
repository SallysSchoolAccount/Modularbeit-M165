from kleine_funktionen import spezifisch_anzeigen

def einfuegen(collection):
    dokumente = []

    while True:
        print("\nNeues Dokument einfügen:")
        dokument = {}

        while True:
            field = input("Name des Felds eingeben (oder Enter zum Beenden):").strip()
            if not field:
                break
            value = input(f"Wert für {field} eingeben:")

            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass  # Behalte es als String, wenn es keine Zahl ist

            dokument[field] = value

        if dokument:
            dokumente.append(dokument)
            print("Dokument erfolgreich zur Liste hinzugefügt")
        else:
            print("Keine Felder wurden zu diesem Dokument hinzugefügt")

        nochmal = input("Noch ein Element einfügen? (y/n):").lower()
        if nochmal != "y":
            break

    if not dokumente:
        print("Keine Dokumente wurden hinzugefügt. Vorgang abgebrochen.")
        return None

    try:
        result = collection.insert_many(dokumente)
        if result.inserted_ids:
            print(f"{len(result.inserted_ids)} Dokumente erfolgreich eingefügt")
            return result.inserted_ids
        else:
            print("Fehler beim Einfügen der Dokumente")
            return None
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {str(e)}")
        return None


def aendern(collection):
    gezeigte_felder = spezifisch_anzeigen()

    for dokument in collection.find():
        for key, value in dokument.items():
            print(f"{key}: {value}")
        print("\n")

    bestimmtes_feld = input("Welchen Feld verändern ?"
                            "\nName, Jahr, Downloads, Bewertung, Genre, Pegi")
    alter_wert = input("Alter Wert eingeben")
    neuer_wert = input("Neuer Wert eingeben")
    alte_sachen = {bestimmtes_feld: alter_wert}
    neue_sachen = {"$set": {bestimmtes_feld: neuer_wert}}
