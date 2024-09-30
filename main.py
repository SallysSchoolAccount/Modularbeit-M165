import pymongo
from sta_minchia import alles_zeigen
from sta_minchia import suche_nach_int

verbindung = pymongo.MongoClient("mongodb://localhost:27017/")
datenbank = verbindung["Spiele"]
collection = datenbank["Spielsammlung"]


def main():
    while True:
        eingabe = input("Enter a command:")
        if eingabe.lower() == "alles":
            alles_zeigen(collection)
        elif eingabe.lower() == "zahl suche":
            suche_nach_int(collection)
        elif eingabe.lower() == "quit":
            print("Die Anwendung wird geschlossen")
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
