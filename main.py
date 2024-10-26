import pymongo
from rich import print
from rich.align import Align
from rich.console import Console
from kleine_funktionen import clear_console
from read import alles_zeigen, suche_nach_int, suche_nach_name, suche_in_array, schnell_zeigen
from create_and_update import einfuegen, update_documents

# Verbindung zur Datenbank
verbindung = pymongo.MongoClient("mongodb://localhost:27017/")
datenbank = verbindung["Spiele"]
collection = datenbank["Spielsammlung"]

console = Console()


def main_menu():
    clear_console()
    while True:
        console.print(Align("[bold magenta]Willkommen zu WormDBsearch[/bold magenta]", align="center"))
        console.print(Align("1: [green]Anzeige Funktionen[/green]", align="center"))
        console.print(Align("2: [green]Neue Dokumente einfügen[/green]", align="center"))
        console.print(Align("3: [green]Dokumente ändern[/green]", align="center"))
        console.print(Align("4: [green]Schnell Anzeige[/green]", align="center"))
        console.print(Align("0: [red]Programm stoppen[/red]", align="center"))

        eingabe = input("Befehl eingeben: ")
        if eingabe == '1':
            clear_console()
            anzeigen_menu()
        elif eingabe == '2':
            einfuegen(collection)
        elif eingabe == '3':
            update_documents(collection)
        elif eingabe == '4':
            schnell_zeigen(collection)
        elif eingabe == '0':
            console.print("[bold red]Die Anwendung wird geschlossen[/bold red]")
            break
        else:
            console.print("[bold red]Invalid command.[/bold red]")


def anzeigen_menu():
    while True:
        console.print(Align("[bold magenta]Anzeigen[/bold magenta]", align="center"))
        console.print(Align("1: [green]Alles zeigen[/green]", align="center"))
        console.print(Align("2: [green]Nach Namen suchen[/green]", align="center"))
        console.print(Align("3: [green]DNach Feldern suchen wo Zahlen als Wert haben[/green]", align="center"))
        console.print(Align("0: [blue]Zurück[/blue]", align="center"))

        eingabe_menu = input("Befehl eingeben: ")
        if eingabe_menu == '1':
            alles_zeigen(collection)
        elif eingabe_menu == '2':
            suche_nach_name(collection)
        elif eingabe_menu == '3':
            suche_nach_int(collection, operatordb=None)
        elif eingabe_menu == '4':
            suche_in_array(collection, suchart=None)
        elif eingabe_menu == '0':
            break
        else:
            print("[bold red]Invalid command.[/bold red]")


print(main_menu())
