from fastapi import APIRouter, Depends
from models.models import Location
from deps import get_weather_service, get_geocoding_service
from services.weather_service import WeatherService
from services.geocoding_service import GeocodingService

router = APIRouter()

@router.get("/weather")
def get_weather(latitude: float, longitude:float, weather_service: WeatherService = Depends(get_weather_service)):
    return weather_service.get_weather_information(latitude, longitude)

@router.get("/cities")
def get_cities(city: str, geocoding_service: GeocodingService = Depends(get_geocoding_service)):
    return geocoding_service.get_cities(city)

