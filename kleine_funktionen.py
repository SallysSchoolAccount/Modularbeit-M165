import os


def clear_console():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
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

        #TODO ========Error when declining sort function, TypeError: Expected a string and a direction=====
        elif eingabe_sortierung == "n":
            return None, None
        else:
            print("Bitte 'y' oder 'n' eingeben.")


def auslassen():
    while True:
        eingabe_skip = input("Resultate auslassen ?")
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
    #TODO ===========Some debug preset so the id shows 'cause its demure=============
    gezeigte_felder = {"_id": 0}
    while True:
        felder_eingabe = input("Welche Felder wolen sie angezeigt haben ?"
                               "\n(Stop tippen um keine Felder mehr zu zeigen )"
                               "\n(Tippen sie hilfe um befehle zu zeigen)").lower()
        if felder_eingabe == "stop":
            break
        elif felder_eingabe == "hilfe":
            print("Presets:"
                  "\nbasic"
                  "\nalle")
        elif felder_eingabe == "basic":
            gezeigte_felder |= {"name": 1, "jahr": 1, "bewertung": 1}
        elif felder_eingabe == "alle":
            gezeigte_felder |= {"name": 1, "jahr": 1, "downloads": 1,  "bewertung": 1, "genre": 1, "pegi": 1}
            break
        else:
            gezeigte_felder |= {felder_eingabe: 1}
    return gezeigte_felder
