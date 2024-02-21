import requests

class GeoAPI:
    API_KEY = "INSERT_API"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"

    # Peticio get para obtener la temperatura actual de Pehuajo
    @classmethod
    def is_hot_in_pehuajo(cls):
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temperature_kelvin = data.get('main', {}).get('temp')
            temperature_celsius = temperature_kelvin - 273.15
            if temperature_celsius > 28:
                return True
            else:
                return False
        else:
            print("Failed to retrieve weather data") 
            return False # Devuelve False incluso si tiene un fallo en la peticion http