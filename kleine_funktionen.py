import os
from rich import print


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def sortierung():
    while True:
        eingabe_sortierung = input("Resultate sortieren ? (y/n)").lower()
        if eingabe_sortierung == "y":
            sortierungs_element = input("Name, Jahr, Downloads, Bewertung, PEGI ?").lower()
            while True:
                ascdesc_input = input("Aufsteigend oder Absteigend ?").lower()
                if ascdesc_input == "aufsteigend":
                    ascdesc = 1
                    break
                elif ascdesc_input == "absteigend":
                    ascdesc = -1
                    break
                else:
                    print("Bitte 'Aufsteigend' oder 'Absteigend' eingeben.")
            return sortierungs_element, ascdesc
        elif eingabe_sortierung == "n":
            return "name", 1
        else:
            print("Bitte 'y' oder 'n' eingeben.")


def auslassen():
    while True:
        eingabe_skip = input("Resultate auslassen ? (y/n)")
        if eingabe_skip == "y":
            skip_anzahl = int(input("Wie viele ?"))
            return skip_anzahl
        elif eingabe_skip == "n":
            skip_anzahl = 0
            return skip_anzahl
        else:
            print("Bitte 'y' oder 'n' eingeben.")


def limitieren():
    while True:
        limit_eingabe: str = input("Wie viele Resultate anzeigen ?")
        if limit_eingabe < "-1":
            print("Zahl nicht gültig")
        elif limit_eingabe == "alle":
            limit_anzahl = 0
            return limit_anzahl
        else:
            limit_anzahl = int(limit_eingabe)
            return limit_anzahl


def spezifisch_anzeigen():
    gezeigte_felder = {"_id": 0}
    while True:
        felder_eingabe = input("Welche Felder wolen sie angezeigt haben ?"
                               "\n('Stop' tippen um keine Felder mehr zu zeigen )"
                               "\n(alle: Zeigt alle Felder an)").lower()
        if felder_eingabe == "stop":
            break
        elif felder_eingabe == "alle":
            gezeigte_felder |= {"name": 1,
                                "jahr": 1,
                                "downloads": 1,
                                "bewertung": 1,
                                "genre": 1,
                                "pegi": 1}
            break
        else:
            gezeigte_felder |= {felder_eingabe: 1}
    return gezeigte_felder
