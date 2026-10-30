from services.weather_service import WeatherService
from services.geocoding_service import GeocodingService
from dotenv import load_dotenv
import os

load_dotenv(".env")

def get_weather_service() -> WeatherService:
    forecast_url = os.environ["OPEN_METEO_FORECAST_URL"]
    return WeatherService(forecast_url)

def get_geocoding_service() -> GeocodingService:
    geocoding_url = os.environ["OPEN_METEO_GEOCODING_URL"]
    return GeocodingService(geocoding_url)