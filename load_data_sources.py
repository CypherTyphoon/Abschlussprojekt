import pandas as pd
import os
import subprocess

def load_other_data_sources():
    print("\nWähle eine Datenquelle:")
    print("1. Excel-Dateien laden")
    print("2. SQL-Datenbank verbinden")
    print("3. Weitere Datenquellen")

    choice = input("Gib die Nummer deiner Wahl ein: ")

    if choice == '1':
        load_excel_file()
    elif choice == '2':
        connect_to_sql_database()
    elif choice == '3':
        load_other_sources()  # Funktion für "Weitere Datenquellen"
    else:
        print("Ungültige Eingabe, bitte versuche es erneut.")

def load_excel_file():
    # Hier kannst du den Code einfügen, um Excel-Dateien zu laden
    file_path = input("Gib den Pfad zur Excel-Datei ein: ")
    try:
        df = pd.read_excel(file_path)
        print("Excel-Datei erfolgreich geladen!")
        print(df.head())  # Zeigt die ersten 5 Zeilen der Datei an
    except Exception as e:
        print(f"Fehler beim Laden der Excel-Datei: {e}")

def connect_to_sql_database():
    # Beispielhafte SQL-Datenbankverbindung
    import sqlite3
    
    db_file = input("Gib den Pfad zur SQLite-Datenbank ein: ")
    
    try:
        conn = sqlite3.connect(db_file)
        print("Erfolgreich mit der Datenbank verbunden!")
        # Hier kannst du SQL-Abfragen ausführen oder Daten extrahieren
        conn.close()
    except Exception as e:
        print(f"Fehler bei der Verbindung zur Datenbank: {e}")

def load_other_sources():
    # Beispiel für weitere Datenquellen
    print("Hier kannst du Code für andere Datenquellen hinzufügen...")

if __name__ == "__main__":
    load_other_data_sources()