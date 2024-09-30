def alles_zeigen(collection):
    if collection.count_documents({}) == 0:
        print("Keine Dokumente in dieser Datenbank")
    for dokument in collection.find():
        print(dokument)


def suche_nach_name(collection):
    eingabe_name = input("Nach was suchen sie ?")
    namen_suche = {"name": {"$regex": eingabe_name}}
    for dokument in collection.find(namen_suche):
        print(dokument)


def suche_nach_jahr(collection):
    eingabe_jahr = input("Nach welchen Jahr suchen sie ?")
    mehr_oder_weniger = input("Mehr oder Weniger als ?")
    if mehr_oder_weniger == "mehr":
        jahr_suche_mehr = {"jahr": {"$gte": eingabe_jahr}}
        for dokument in collection.find(jahr_suche_mehr):
            print(dokument)
    elif mehr_oder_weniger == "weniger":
        jahr_suche_weniger = {"jahr": {"$lte": eingabe_jahr}}
        for dokument in collection.find(jahr_suche_weniger):
            print(dokument)
    else: eingabe_jahr