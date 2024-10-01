def alles_zeigen(collection):

    #Begin of sorting mechanism
    eingabe_sortierung = input("Sortieren ? (y/n)").lower()
    if eingabe_sortierung == "y":
        sortierungs_element = input("Name, Jahr, Downloads, Bewertung, PEGI ?").lower()
        ascdesc_input = input("Aufsteigend oder Absteigend ?")
        if ascdesc_input == "aufsteigend":
            ascdesc = 1
        elif ascdesc_input == "absteigend":
            ascdesc = -1
        else: print("Aufsteigend oder Absteigend ?")
    elif eingabe_sortierung == "n":
        sortierungs_element = None
    else: print("Sortieren ? (y/n)")
    #End of sorting mechanism

    for dokument in collection.find().sort(sortierungs_element, ascdesc):
        print(dokument)


def suche_nach_name(collection):
    eingabe_name = input("Nach was suchen sie ?").lower()

    #Name suchen
    namen_suche = {"name": {"$regex": eingabe_name}}

    #Begin of sorting mechanism
    eingabe_sortierung = input("Sortieren ? (y/n)").lower()
    if eingabe_sortierung == "y":
        sortierungs_element = input("Name, Jahr, Downloads, Bewertung, PEGI ?").lower()
        ascdesc_input = input("Aufsteigend oder Absteigend ?")
        if ascdesc_input == "aufsteigend":
            ascdesc = 1
        elif ascdesc_input == "absteigend":
            ascdesc = -1
        else: print("Aufsteigend oder Absteigend ?")
    elif eingabe_sortierung == "n":
        sortierungs_element = None
    else: print("Sortieren ? (y/n)")
    #End of sorting mechanism

    for dokument in collection.find(namen_suche).sort(sortierungs_element, ascdesc):
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
    else: print("Mehr, weniger oder gleich ?")
    eingabe_nummer = int(input("Nach welche Zahl ?"))
    #End of search

    #Begin of sorting mechanism
    eingabe_sortierung = input("Sortieren ? (y/n)").lower()
    if eingabe_sortierung == "y":
        sortierungs_element = input("Name, Jahr, Downloads, Bewertung, PEGI ?").lower()
        ascdesc_input = input("Aufsteigend oder Absteigend ?")
        if ascdesc_input == "aufsteigend":
            ascdesc = 1
        elif ascdesc_input == "absteigend":
            ascdesc = -1
        else: print("Aufsteigend oder Absteigend ?")
    elif eingabe_sortierung == "n":
        sortierungs_element = None
    else: print("Sortieren ? (y/n)")
    #End of sorting mechanism

    #Search query
    such_query = {eingabe_modus: {operatorDB: eingabe_nummer}}
    for dokument in collection.find(such_query).sort(sortierungs_element, ascdesc):
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

    #Begin of sorting mechanism
    eingabe_sortierung = input("Sortieren ? (y/n)").lower()
    if eingabe_sortierung == "y":
        sortierungs_element = input("Name, Jahr, Downloads, Bewertung, PEGI ?").lower()
        ascdesc_input = input("Aufsteigend oder Absteigend ?")
        if ascdesc_input == "aufsteigend":
            ascdesc = 1
        elif ascdesc_input == "absteigend":
            ascdesc = -1
        else: print("Aufsteigend oder Absteigend ?")
    elif eingabe_sortierung == "n":
        sortierungs_element = None
    else: print("Sortieren ? (y/n)")
    #End of sorting mechanism

    for dokument in collection.find({array_field: {suchart: value_list}}).sort(sortierungs_element, ascdesc):
        print(dokument)