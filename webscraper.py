import os
import pandas as pd
import requests
from bs4 import BeautifulSoup

def webscraper():
    # Ordner erstellen, falls nicht vorhanden
    output_dir = "02_Webscrapper-Ergebnisse"
    os.makedirs(output_dir, exist_ok=True)

    # Beispiel-URL (ändere sie je nach Bedarf)
    url = "https://example.com"
    
    # Scraping durchführen
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Beispielhafte Daten extrahieren (ändere die Selektoren je nach Bedarf)
    data = []
    for item in soup.select('css-selector'):
        data.append({
            'title': item.get_text(),
            'link': item['href']
        })

    # Daten in ein DataFrame umwandeln
    df = pd.DataFrame(data)

    # DataFrame als CSV speichern
    csv_file_path = os.path.join(output_dir, 'scraped_data.csv')
    df.to_csv(csv_file_path, index=False)

    # Kurze Beschreibung der Daten
    print(f"{len(df)} Datensätze wurden erfolgreich aus {url} extrahiert und in {csv_file_path} gespeichert.")

    # Beispielhafte Anzeige der ersten 5 Daten
    print("Beispielhafte Daten:")
    print(df.head())

if __name__ == "__main__":
    webscraper()