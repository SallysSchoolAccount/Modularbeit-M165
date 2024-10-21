from kleine_funktionen import sortierung
from kleine_funktionen import auslassen
from kleine_funktionen import limitieren
from kleine_funktionen import spezifisch_anzeigen


def alles_zeigen(collection):
    #Sotierung Funktion
    sortierungs_element, ascdesc = sortierung()

    #Auslassen Funktion
    skip_anzahl = auslassen()

    #Limit Funktion
    limit_anzahl = limitieren()

    #Felder auswaehlen
    gezeigte_felder = spezifisch_anzeigen()

    for dokument in (collection
            .find({}, gezeigte_felder)
            .sort(sortierungs_element, ascdesc)
            .skip(skip_anzahl)
            .limit(limit_anzahl)):
        print(dokument)


def suche_nach_name(collection):
    eingabe_name = input("Nach was suchen sie ?").lower()

    #Name suchen und Suchquery
    namen_suche = {"name": {"$regex": eingabe_name}}

    #Sortierung Funktion
    sortierungs_element, ascdesc = sortierung()

    # Auslassen Funktion
    skip_anzahl = auslassen()

    # Limit Funktion
    limit_anzahl = limitieren()

    # Felder auswaehlen
    gezeigte_felder = spezifisch_anzeigen()

    for dokument in (collection
            .find(namen_suche)
            .sort(sortierungs_element, ascdesc)
            .skip(skip_anzahl)
            .limit(limit_anzahl)):
        print(dokument)


def suche_nach_int(collection):
    #Begin of search
    eingabe_modus = input("Jahr, Downloads, Bewertung, PEGI ?").lower()
    eingabe_operator = input("Mehr, weniger oder gleich ?").lower()
    if eingabe_operator == "mehr":
        operatorDB = "$gte"
    elif eingabe_operator == "weniger":
        operatorDB = "$lte"
    elif eingabe_operator == "gleich":
        operatorDB = "$eq"
    else:
        print("Mehr, weniger oder gleich ?")
    eingabe_nummer = int(input("Nach welche Zahl ?"))
    #End of search

    # Sortierung Funktion
    sortierungs_element, ascdesc = sortierung()

    # Auslassen Funktion
    skip_anzahl = auslassen()

    # Limit Funktion
    limit_anzahl = limitieren()

    # Felder auswaehlen
    gezeigte_felder = spezifisch_anzeigen()

    #Search query
    such_query = {eingabe_modus: {operatorDB: eingabe_nummer}}
    for dokument in (collection
            .find(such_query, gezeigte_felder)
            .sort(sortierungs_element, ascdesc)
            .skip(skip_anzahl)
            .limit(limit_anzahl)):
        print(dokument)


def suche_in_array(collection):
    value_list = []
    array_field = input("In welchen Feld suchen sie ?")

    #Elemente zur suchliste hinzufuegen
    while True:
        elemente = input("Welche Elemente suchen sie ?")
        if elemente == "enough":
            break
        else:
            value_list.append(elemente)

    #Suchart waehlen
    suchart_eingabe = input("multiple or all ?").lower()
    if suchart_eingabe == "multiple":
        suchart = "$in"
    elif suchart_eingabe == "all":
        suchart = "$all"

    #Sortierung Funktion
    sortierungs_element, ascdesc = sortierung()

    # Auslassen Funktion
    skip_anzahl = auslassen()

    # Limit Funktion
    limit_anzahl = limitieren()

    # Felder auswaehlen
    gezeigte_felder = spezifisch_anzeigen()

    #Suchquery
    such_query = {array_field: {suchart: value_list}}
    for dokument in (collection
            .find(such_query, gezeigte_felder)
            .sort(sortierungs_element, ascdesc)
            .skip(skip_anzahl)
            .limit(limit_anzahl)):
        print(dokument)
