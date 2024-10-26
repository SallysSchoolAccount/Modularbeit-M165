from read import schnell_zeigen
from rich.console import Console
from typing import List
from kleine_funktionen import clear_console


def einfuegen(collection):
    clear_console()
    schnell_zeigen(collection)

    # Benutzer gibt Wert fuer jedes Feld ein
    name = input("Enter the name: ")
    jahr = int(input("Enter the year: "))
    downloads = int(input("Enter the number of downloads: "))
    bewertung = float(input("Enter the rating: "))

    # Genre ist eine liste, very annoying
    genre_input = input("Enter genres (comma-separated): ")
    genre: List[str] = [g.strip() for g in genre_input.split(',')]

    # Wert fuer pegi feld
    pegi = int(input("Enter the PEGI rating: "))

    # Dokument herstellen
    new_document = {
        "name": name,
        "jahr": jahr,
        "downloads": downloads,
        "bewertung": bewertung,
        "genre": genre,
        "pegi": pegi
    }

    # Dokumente einuegen
    result = collection.insert_one(new_document)

    #Check
    if result.inserted_id:
        print(f"Document inserted successfully with id: {result.inserted_id}")
        schnell_zeigen(collection)
    else:
        print("Failed to insert document")


def update_documents(collection):

    console = Console()

    # Display all documents
    console.print("Current documents in the collection:", style="bold green")

    # Get user input for the update
    filter_field = input("Enter the field to filter by")
    filter_value = input("Enter the value to filter by")
    update_field = input("Enter the field to update")
    update_value = input("Enter the new value")

    # Perform the update
    try:
        result = collection.update_many(
            {filter_field: filter_value},
            {"$set": {update_field: update_value}}
        )
        print(f"\n[bold green]Updated {result.modified_count} document(s)[/bold green]")
    except Exception as e:
        print(f"[bold red]An error occurred during the update: {str(e)}[/bold red]")
        return

    # Display updated documents
    console.print("\nUpdated documents in the collection:", style="bold green")
    schnell_zeigen(collection)
