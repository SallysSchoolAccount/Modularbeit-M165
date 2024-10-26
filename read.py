from rich.console import Console
from rich.table import Table
from kleine_funktionen import sortierung, auslassen, limitieren, spezifisch_anzeigen, clear_console


def schnell_zeigen(collection):
    # Fetch documents
    documents = list(collection.find({}, {"_id": 0,
                                          "name": 1,
                                          "jahr": 1,
                                          "downloads": 1,
                                          "bewertung": 1,
                                          "genre": 1,
                                          "pegi": 1}))

    #Console herstellen
    console = Console()

    # Tabelle herstellen
    table = Table(title="Dokumente")
    for key in documents[0].keys():
        table.add_column(key)
    for dokument in documents:
        table.add_row(*[str(value) for value in dokument.values()])

    console.print(table)
    input("Drücken sie eine Taste um weiterzugehen...")
    clear_console()


def alles_zeigen(collection):
    clear_console()

    # Sortierung Funktion
    sortierungs_element, ascdesc = sortierung()

    # Auslassen Funktion
    skip_anzahl = auslassen()

    # Limit Funktion
    limit_anzahl = limitieren()

    # Felder auswaehlen
    gezeigte_felder = spezifisch_anzeigen()

    # Fetch documents
    documents = list(collection
                     .find({}, gezeigte_felder)
                     .sort(sortierungs_element, ascdesc)
                     .skip(skip_anzahl)
                     .limit(limit_anzahl))

    if not documents:
        print("Keine Dokumente gefunden.")
        input("Drücken sie eine Taste um weiterzugehen...")
        return

    # Tabelle herstellen
    table = Table(title="Dokumente")
    for key in documents[0].keys():
        table.add_column(key)
    for dokument in documents:
        table.add_row(*[str(value) for value in dokument.values()])

    # Create a Console object
    console = Console()

    # Tabelle ausführen
    console.print(table)
    input("Drücken sie eine Taste um weiterzugehen...")
    clear_console()


def suche_nach_name(collection):
    clear_console()

    eingabe_name = input("Nach was suchen sie?").lower()

    # Name suchen und Suchquery
    namen_suche = {"name": {"$regex": eingabe_name, "$options": "i"}}  # Adding case-insensitive search

    # Sortierung Funktion
    sortierungs_element, ascdesc = sortierung()

    # Auslassen Funktion
    skip_anzahl = auslassen()

    # Limit Funktion
    limit_anzahl = limitieren()

    # Felder auswaehlen
    gezeigte_felder = spezifisch_anzeigen()

    # Fetch Documents
    query = namen_suche
    documents = list(collection
                     .find(query, gezeigte_felder)
                     .sort(sortierungs_element, ascdesc)
                     .skip(skip_anzahl)
                     .limit(limit_anzahl))

    if not documents:
        print("Keine Dokumente gefunden.")
        input("Drücken sie eine Taste um weiterzugehen...")
        return

    # Tabelle herstellen
    table = Table(title="Dokumente")
    for key in documents[0].keys():
        table.add_column(key)
    for dokument in documents:
        table.add_row(*[str(value) for value in dokument.values()])

    # Console Objekt herstellen
    console = Console()

    # Tabelle ausführen
    console.print(table)
    input("Drücken sie eine Taste um weiterzugehen...")


def suche_nach_int(collection, operatordb):
    clear_console()

    #Suche beginnen
    eingabe_modus = input("Jahr, Downloads, Bewertung, PEGI ?").lower()
    eingabe_operator = input("Mehr, weniger oder gleich ?").lower()
    if eingabe_operator == "mehr":
        operatordb = "$gte"
    elif eingabe_operator == "weniger":
        operatordb = "$lte"
    elif eingabe_operator == "gleich":
        operatordb = "$eq"
    else:
        print("Mehr, weniger oder gleich ?")
    eingabe_nummer = int(input("Nach welche Zahl ?"))
    #Suche beenden

    # Sortierung Funktion
    sortierungs_element, ascdesc = sortierung()

    # Auslassen Funktion
    skip_anzahl = auslassen()

    # Limit Funktion
    limit_anzahl = limitieren()

    # Felder auswaehlen
    gezeigte_felder = spezifisch_anzeigen()

    #Search query
    such_query = {eingabe_modus: {operatordb: eingabe_nummer}}
    #Fetch Documents
    documents = list(collection
                     .find({such_query}, gezeigte_felder)
                     .sort(sortierungs_element, ascdesc)
                     .skip(skip_anzahl)
                     .limit(limit_anzahl))

    if not documents:
        print("Keine Dokumente gefunden.")
        input("Drücken sie eine Taste um weiterzugehen...")
        return

    # Tabelle herstellen
    table = Table(title="Dokumente")
    for key in documents[0].keys():
        table.add_column(key)
    for dokument in documents:
        table.add_row(*[str(value) for value in dokument.values()])

    # Console Objekt herstellen
    console = Console()

    # Tabelle ausführen
    console.print(table)
    input("Drücken sie eine Taste um weiterzugehen...")


def suche_in_array(collection, suchart):
    clear_console()
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
    #Fetch Documents
    documents = list(collection
                     .find({such_query}, gezeigte_felder)
                     .sort(sortierungs_element, ascdesc)
                     .skip(skip_anzahl)
                     .limit(limit_anzahl))

    if not documents:
        print("Keine Dokumente gefunden.")
        input("Drücken sie eine Taste um weiterzugehen...")
        return

    # Tabelle herstellen
    table = Table(title="Dokumente")
    for key in documents[0].keys():
        table.add_column(key)
    for dokument in documents:
        table.add_row(*[str(value) for value in dokument.values()])

    # Console Objekt herstellen
    console = Console()

    # Tabelle ausführen
    console.print(table)
    input("Drücken sie eine Taste um weiterzugehen...")
