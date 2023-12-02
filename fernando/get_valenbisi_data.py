import requests
import json

def get_valenbisi_data():
    url = 'https://www.valenbisi.es/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=20'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    stations_data = get_valenbisi_data()

    if stations_data:
        with open('valenbisi_stations.json', 'w') as file:
            json.dump(stations_data, file)
        print("Valenbisi stations data fetched and saved to valenbisi_stations.json")
