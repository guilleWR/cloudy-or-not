import httpx

class WeatherService:

    def __init__(self, url):
        self.forecast_url = url

    def get_weather_information(self, latitude: float, longitude: float) -> dict:
        params = {
            'latitude': latitude, 
            'longitude': longitude, 
            'current': [
                'temperature_2m', 
                'relative_humidity_2m', 
                'wind_speed_10m', 
                'apparent_temperature'
            ],
            'timezone': "Europe/Madrid" 
        }
        resp = httpx.get(self.forecast_url, params=params)
        dic = resp.json()
        result = {
            "latitude": latitude,
            "longitude": longitude,
            "current temperature": dic.get("current").get("temperature_2m"),
            "apparent temperature": dic.get("current").get("apparent_temperature"),
            "temperature unit" : dic.get("current_units").get("temperature_2m"),
            "relative humidity": dic.get("current").get("relative_humidity_2m"),
            "humidity unit": dic.get("current_units").get("relative_humidity_2m"),
            "wind velocity": dic.get("current").get("wind_speed_10m"),
            "velocity unit": dic.get("current_units").get("wind_speed_10m"),
            "time": dic.get("current").get("time")
        }
                   
        return result