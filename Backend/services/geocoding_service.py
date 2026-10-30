import httpx

class GeocodingService:

    MAX_NUMBER_CITIES = 5

    def __init__(self, url):
        self.geocoding_url = url

    def get_cities(self, city: str) -> dict:
        params = {'name': city}
        resp = httpx.get(self.geocoding_url, params=params)
        dic = resp.json()

        if not dic.get("results"):
            cities = []
        else :
            cities = self._search_cities(self.MAX_NUMBER_CITIES, dic)
        
        return {'cities': cities}


    def _search_cities(self, max_cities: int, dic: dict) -> list:
        counter = 0
        cities = []

        for city in dic.get("results"):
            cities.append(self._filter_city(city))
            counter+=1
            if counter == max_cities:
                break

        return cities

    def _filter_city(self, city: dict) -> dict:
        filtered_city = {
            'id': city.get("id"),
            'name': city.get("name"),
            'country': city.get("country"),
            'latitude': city.get("latitude"),
            'longitude': city.get("longitude")
        }
        # If a region exists we add it. (this is optional)
        if city.get("admin1"): 
            filtered_city["region"] = city.get("admin1")

        return filtered_city

  