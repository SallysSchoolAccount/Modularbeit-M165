def einfuegen(collection):
    dokumente = []

    while True:
        print("\nNeues Dokument einfügen:")
        dokument = {}

        while True:
            field = input("Name des Felds eingeben:").strip()
            if not field:
                break
            value = input(f"Wert für {field} eingeben:")

            try:
                value = int(value)
            except ValueError:
                pass

            dokument[field] = value

        if dokument:
            dokumente.append(dokument)
            print("Dokument erfolgreich eingefügt")
        else:
            print("Keine Felder wurden zu diesen Dokument eingefügt")

        nochmal = input("Noch ein Element einfügen ?:").lower()
        if nochmal != "y":
            break

        if not dokumente:
            print("")
            return None

        result = collection.insert_many(dokumente)

        if result.inserted_ids:
            print(f"{len(result.inserted_ids)}Dokument erfolgreich eingefügt")
            return result.inserted_ids
        else:
            print("Error")
            return None