from read import schnell_zeigen
from rich.console import Console
from rich.table import Table
from typing import List


def einfuegen(collection):

    # Benutzer gibt Wert fuer jedes Feld ein
    name = input("Name eingeben: ")
    jahr = int(input("Erscheinungsjahr eingeben: "))
    downloads = int(input("Anzahl downloads eingeben: "))
    bewertung = float(input("Bewertung eingeben: "))

    # Genre ist eine liste, very annoying
    genre_input = input("Genres eingeben (mit ein komma geteilt): ")
    genre: List[str] = [g.strip() for g in genre_input.split(',')]

    # Wert fuer pegi feld
    pegi = int(input("Altersgrenze eingeben: "))

    # Dokument herstellen
    neues_dokument = {
        "name": name,
        "jahr": jahr,
        "downloads": downloads,
        "bewertung": bewertung,
        "genre": genre,
        "pegi": pegi
    }

    # Dokumente einfuegen
    result = collection.insert_one(neues_dokument)

    #Check
    if result.inserted_id:
        print(f"Document inserted successfully with id: {result.inserted_id}")
        schnell_zeigen(collection)
    else:
        print("Failed to insert document")


def update_documents(collection):
    # Display all documents
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
    console.print("Current documents in the collection:", style="bold green")

    # Get user input for the update
    altes_feld = input("Feld eingeben")
    altes_wert = input("Jetziges Wert eingeben")
    neues_feld = input("Neues Feld eingeben")
    neues_wert = input("Neues Wert eigeben")

    # Perform the update
    try:
        result = collection.update_many(
            {altes_feld: altes_wert},
            {"$set": {neues_feld: neues_wert}}
        )
        print(f"\n[bold green]Verändert {result.modified_count} document(s)[/bold green]")
    except Exception as e:
        print(f"[bold red]Es gab ein Fehler bei der : {str(e)}[/bold red]")
        return

    # Display updated documents
    console.print("\nUpdated documents in the collection:", style="bold green")
    schnell_zeigen(collection)


def loeschen(collection):
    feld_loeschen = input("Feld eingeben:")
    wert_loeschen = input("Wert eigeben:")

    #Verwandelt das Wert zu ein int
    try:
        wert_loeschen = int(wert_loeschen)
    except ValueError:
        pass

    loesch_query = {feld_loeschen: wert_loeschen}

    #Bestätigung
    conferma = input("Tippen sie 'löschen' um es zu bestätigen")
    if conferma == "löschen":
        collection.delete_one(loesch_query)
        print("Das Dokument wurde gelöscht")
    else:
        print("Das Dokument wurde nicht gelöscht")
