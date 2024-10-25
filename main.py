import pymongo
from rich import print
from rich.align import Align
from kleine_funktionen import clear_console
from read import alles_zeigen, suche_nach_int, suche_nach_name, suche_in_array
from create_and_update import einfuegen, aendern

# Verbindung zur Datenbank
verbindung = pymongo.MongoClient("mongodb://localhost:27017/")
datenbank = verbindung["Spiele"]
collection = datenbank["Spielsammlung"]


def main_menu():
    clear_console()
    while True:
        print("[bold magenta]Main Menu[/bold magenta]")
        print("1: [green]Anzeige Funktionen[/green]")
        print("2: [green]Neue Dokumente einfügen[/green]")
        print("3: [green]Dokumente ändern[/green]")
        print("0: [red]Programm stoppen[/red]")
        eingabe = input("Befehl eingeben: ")
        if eingabe == '1':
            anzeigen_menu()
        elif eingabe == '2':
            einfuegen(collection)
        elif eingabe == '3':
            aendern(collection)
        elif eingabe == '0':
            print("[bold red]Die Anwendung wird geschlossen[/bold red]")
            break
        else:
            print("[bold red]Invalid command.[/bold red]")


def anzeigen_menu():
    clear_console()
    while True:
        print("[bold magenta]Anzeige Menu[/bold magenta]")
        print("1: [green]Alle Elemente anzeigen[/green]")
        print("2: [green]Nach Namen suchen[/green]")
        print("3: [green]Nach Feldern suchen wo Zahlen als Wert haben[/green]")
        print("4: [green]In Listen suchen[/green]")
        print("0: [blue]Zurück[/blue]")
        eingabe_menu = input("Befehl eingeben: ")
        if eingabe_menu == '1':
            alles_zeigen(collection)
        elif eingabe_menu == '2':
            suche_nach_name(collection)
        elif eingabe_menu == '3':
            suche_nach_int(collection, operatordb= None)
        elif eingabe_menu == '4':
            suche_in_array(collection, suchart= None)
        elif eingabe_menu == '0':
            break
        else:
            print("[bold red]Invalid command.[/bold red]")

print(main_menu())