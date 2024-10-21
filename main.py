import pymongo
from kleine_funktionen import clear_console
from read import alles_zeigen
from read import suche_nach_int
from read import suche_nach_name
from read import suche_in_array
from create_and_update import einfuegen

#Verbindung zur Datenbank
verbindung = pymongo.MongoClient("mongodb://localhost:27017/")
datenbank = verbindung["Spiele"]
collection = datenbank["Spielsammlung"]


def main():
    while True:
        clear_console()
        eingabe = input("\nAnzeigen:\nAnzeige Funktionen\n"
                        "\nEinfügen:\nNeue Dokumente einfügen\n"
                        "\nÄndern:\nDokumente einfügen\n"
                        "\nquit:\nProgramm stoppen\n"
                        "\nEnter a command: ")
        if eingabe.lower() == "anzeigen":
            anzeigen_menu(eingabe_menu=input())
        elif eingabe.lower() == "einfügen":
            einfuegen(collection)
        elif eingabe.lower() == "quit":
            print("Die Anwendung wird geschlossen")
            break
        else:
            print("Invalid command.")


def anzeigen_menu(eingabe_menu):
    while True:
        clear_console()
        eingabe_menu = input("\nDokumente:\nAlle Elemente anzeigen\n"
                             "\nNamen suche:\nNach namen suchen\n"
                             "\nZahl suche:\nNach Felder suchen wo Zahlen als Wert haben\n"
                             "\nListen suche:\nIn Listen suchen\n")
        if eingabe_menu.lower() == "dokumente":
            alles_zeigen(collection)
        elif eingabe_menu.lower() == "namen suche":
            suche_nach_name(collection)
        elif eingabe_menu.lower() == "zahl suche":
            suche_nach_int(collection)
        elif eingabe_menu.lower() == "listen suche":
            suche_in_array(collection)
        elif eingabe_menu.lower() == "quit":
            break
        else:
            print("Invalid command")

print(main())
