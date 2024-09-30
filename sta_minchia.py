def alles_zeigen(collection):
    if collection.count_documents({}) == 0:
        print("Keine Dokumente in dieser Datenbank")
    for dokument in collection.find():
        print(dokument)


def suche_nach_name(collection):
    eingabe_name = input("Nach was suchen sie ?").lower()
    namen_suche = {"name": {"$regex": eingabe_name}}
    for dokument in collection.find(namen_suche):
        print(dokument)


def suche_nach_int(collection):
    eingabe_modus = input("Jahr, Downloads, Bewertung, PEGI ?").lower()
    eingabe_operator = input("Mehr, weniger oder gleich ?").lower()
    if eingabe_operator == "mehr":
        operatorDB = "$gte"
    elif eingabe_operator == "weniger":
        operatorDB = "$lte"
    elif eingabe_operator == "gleich":
        operatorDB = "$eq"
    else: eingabe_operator
    eingabe_nummer = int(input("Nach welche Zahl ?"))
    such_query = {eingabe_modus: {operatorDB: eingabe_nummer}}
    for dokument in collection.find(such_query):
        print(dokument)