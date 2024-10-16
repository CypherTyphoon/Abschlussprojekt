import subprocess
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def menu():
    while True:
        print("\nWähle eine Option:")
        print("1. Vorhandene Daten nutzen")
        print("2. Webscraping-Daten laden")
        print("3. Andere Datenquellen laden")
        print("4. Anzeige bisheriger gespeicherter Analysen")
        print("5. Ausgabe des Datenanalyse_Log")
        print("6. Beenden")

        choice = input("Gib die Nummer deiner Wahl ein: ")

        if choice == '1':
            use_existing_data()
        elif choice == '2':
            load_webscraping_data()
        elif choice == '3':
            load_other_data_sources()
        elif choice == '4':
            display_saved_analyses()
        elif choice == '5':
            display_data_analysis_log()
        elif choice == '6':
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

def use_existing_data():
    # Hier kannst du den Code einfügen, um vorhandene Daten zu nutzen
    print("Vorhandene Daten werden genutzt...")
    subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "Vorhandene_Daten.ipynb"])

def load_webscraping_data():
    # Hier wird die webscraper.py ausgeführt
    print("Webscraping-Daten werden geladen...")
    subprocess.run(["python", "webscraper.py"])  # Stelle sicher, dass der Pfad korrekt ist

def load_other_data_sources():
    print("Andere Datenquellen werden geladen...")
    subprocess.run(["python", "load_data_sources.py"])

def display_saved_analyses():
    # Pfad zum Ablage-Ordner
    folder_path = '01_Ablage'
    
    # Überprüfen, ob der Ordner existiert
    if not os.path.exists(folder_path):
        print(f"Der Ordner '{folder_path}' existiert nicht.")
        return
    
    # Liste der Bilddateien im Ordner abrufen
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    # Überprüfen, ob Bilder gefunden wurden
    if not image_files:
        print("Keine Bilder im Ordner 'Ablage' gefunden.")
        return
    
    # Bilder anzeigen
    for image_file in image_files:
        img_path = os.path.join(folder_path, image_file)
        img = mpimg.imread(img_path)
        plt.figure()
        plt.imshow(img)
        plt.axis('off')  # Achsen ausblenden
        plt.title(image_file)  # Titel des Bildes setzen
        plt.show()

def display_data_analysis_log():
    # Pfad zur Log-Datei
    log_file_path = os.path.join('01_Ablage', 'Datenanalyse_Log.txt')
    
    # Überprüfen, ob die Log-Datei existiert
    if not os.path.exists(log_file_path):
        print(f"Die Datei '{log_file_path}' existiert nicht.")
        return
    
    # Log-Datei öffnen und ihren Inhalt anzeigen
    with open(log_file_path, 'r') as log_file:
        print("Datenanalyse_Log:")
        print(log_file.read())  # Den gesamten Inhalt der Log-Datei lesen und anzeigen

if __name__ == "__main__":
    menu()