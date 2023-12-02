import requests
import logging

logging.basicConfig(level=logging.INFO)

# URL de la API proporcionada
url = "https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=20"

try:
    # Realiza la solicitud GET
    response = requests.get(url)

    # Verifica si la solicitud fue exitosa (código de estado 200)
    response.raise_for_status()

    # Procesa la respuesta en formato JSON
    data = response.json()

    # Imprime la respuesta completa para depurar
    logging.info(f"API Response: {data}")

    # Accede a los datos específicos
    total_count = data["total_count"]
    records = data.get("records", [])

    # Si hay al menos un registro
    if records:
        record = records[0]
        
        # Accede a los detalles específicos de ese registro
        fields = record.get("fields", {})
        address = fields.get("address")
        number = fields.get("number")
        open_status = fields.get("open")
        available = fields.get("available")
        free = fields.get("free")
        total = fields.get("total")
        ticket = fields.get("ticket")
        updated_at = fields.get("updated_at")
        geo_shape = fields.get("geo_shape", {})
        geo_point_2d = fields.get("geo_point_2d", {})

        # Accede a las coordenadas específicas
        lon = geo_point_2d.get("lon")
        lat = geo_point_2d.get("lat")

        # Ahora puedes usar estas variables según tus necesidades
        logging.info(f"Total count: {total_count}")
        logging.info(f"Address: {address}, Number: {number}")
        logging.info(f"Open status: {open_status}")
        logging.info(f"Available: {available}, Free: {free}, Total: {total}")
        logging.info(f"Ticket: {ticket}")
        logging.info(f"Updated at: {updated_at}")
        logging.info(f"Coordinates: Lon: {lon}, Lat: {lat}")

    else:
        logging.info("No records found.")

except requests.exceptions.RequestException as e:
    logging.error(f"Error en la solicitud: {e}")
finally:
    if 'response' in locals():
        response.close()



