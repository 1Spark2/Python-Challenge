import requests

class GeoAPI:
    API_KEY = "1074e3185236c2e36b519885bbb220cc"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"

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
            return False 
        


if __name__ == "__main__":
    print(GeoAPI.is_hot_in_pehuajo())