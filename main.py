import pymongo
from such_funktionen import alles_zeigen
from such_funktionen import suche_nach_int
from such_funktionen import suche_nach_name
from such_funktionen import suche_in_array

#Verbindung zur Datenbank
verbindung = pymongo.MongoClient("mongodb://localhost:27017/")
datenbank = verbindung["Spiele"]
collection = datenbank["Spielsammlung"]


def main():
    while True:
        eingabe = input("Enter a command:")
        if eingabe.lower() == "dokumente":
            alles_zeigen(collection)
        elif eingabe.lower() == "namen suche":
            suche_nach_name(collection)
        elif eingabe.lower() == "zahl suche":
            suche_nach_int(collection)
        elif eingabe.lower() == "array suche":
            suche_in_array(collection)
        elif eingabe.lower() == "quit":
            print("Die Anwendung wird geschlossen")
            break
        else:
            print("Invalid command.")


print(main())
