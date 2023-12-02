import requests

# URL de la API proporcionada
url = "https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=100"

try:
    # Realiza la solicitud GET
    response = requests.get(url)

    # Verifica si la solicitud fue exitosa (código de estado 200)
    response.raise_for_status()

    # Procesa la respuesta en formato JSON
    data = response.json()

    # Accede a los datos específicos
    total_count = data["total_count"]
    results = data.get("results", [])


    # Si hay al menos un registro
    for result in results:
        address = result.get("address")
        number = result.get("number")
        open_status = result.get("open")
        available = result.get("available")
        free = result.get("free")
        total = result.get("total")
        ticket = result.get("ticket")
        updated_at = result.get("updated_at")
        geo_shape = result.get("geo_shape", {})
        geo_point_2d = result.get("geo_point_2d", {})

        lon = geo_point_2d.get("lon")
        lat = geo_point_2d.get("lat")

        # Ahora puedes usar estas variables según tus necesidades
        print(f"Parada: {number}")
        print(f"Address: {address}, Number: {number}")
        print(f"Open status: {open_status}")
        print(f"Available: {available}, Free: {free}, Total: {total}")
        print(f"Ticket: {ticket}")
        print(f"Updated at: {updated_at}")
        print(f"Coordinates: Lon: {lon}, Lat: {lat}")
        print("-----------------------------------------")

finally:
    if 'response' in locals():
        response.close()
