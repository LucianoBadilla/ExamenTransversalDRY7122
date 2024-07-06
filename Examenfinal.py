import requests
from opencage.geocoder import OpenCageGeocode
from geopy.distance import geodesic

# Función para obtener las coordenadas de una ciudad
def get_coordinates(city, api_key):
    geocoder = OpenCageGeocode(api_key)
    results = geocoder.geocode(city)
    if results:
        return (results[0]['geometry']['lat'], results[0]['geometry']['lng'])
    else:
        print(f"No se pudieron obtener las coordenadas de {city}.")
        return None

# Función para calcular la distancia entre dos puntos geográficos
def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).km

# Solicitar información del usuario
api_key = '6fd1259e0b62439ca9c5f2375b546ccb'
while True:
    origen = input("Ingrese la Ciudad de Origen: ")
    if origen.lower() == 's':
        break
    destino = input("Ingrese la Ciudad de Destino: ")
    if destino.lower() == 's':
        break

    # Obtener coordenadas de las ciudades
    coord_origen = get_coordinates(origen, api_key)
    coord_destino = get_coordinates(destino, api_key)

    if coord_origen and coord_destino:
        # Calcular la distancia
        distancia_km = calculate_distance(coord_origen, coord_destino)
        distancia_millas = distancia_km * 0.621371
        
        # Duración del viaje según el medio de transporte
        medio_transporte = input("Ingrese el medio de transporte (auto, avión, bicicleta): ").lower()
        if medio_transporte == 's':
            break
        
        if medio_transporte == 'auto':
            velocidad_media = 80  # km/h
        elif medio_transporte == 'avión':
            velocidad_media = 800  # km/h
        elif medio_transporte == 'bicicleta':
            velocidad_media = 20  # km/h
        else:
            print("Medio de transporte no válido.")
            continue
        
        duracion_horas = distancia_km / velocidad_media
        
        # Mostrar resultados
        print(f"\nDistancia entre {origen} y {destino}:")
        print(f" - En kilómetros: {distancia_km:.2f} km")
        print(f" - En millas: {distancia_millas:.2f} millas")
        print(f"Duración del viaje en {medio_transporte}: {duracion_horas:.2f} horas\n")
        
        # Narrativa del viaje
        print(f"Narrativa del viaje: Desde {origen} hasta {destino} hay una distancia de {distancia_km:.2f} kilómetros. Viajando en {medio_transporte}, el viaje tomará aproximadamente {duracion_horas:.2f} horas.\n")
    else:
        print("No se pudieron obtener las coordenadas de una o ambas ciudades.")

    salir = input("¿Desea salir? (s/n): ").lower()
    if salir == 's':
        break
