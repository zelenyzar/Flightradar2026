from abc import ABC, abstractmethod

import pycountry
import requests


class RequestAPI(ABC):
    """абстрактный класс, определяющий общие методы работы с API"""

    @abstractmethod
    def get_coordinates(self, country):
        pass

    @abstractmethod
    def get_aeroplanes(self, get_coordinates):
        pass


class Aircrafts(RequestAPI):
    """класс самолетов из API"""

    def __init__(self) -> None:
        self.openstreetmap_url = "https://nominatim.openstreetmap.org/search"
        self.opensky_url = "https://opensky-network.org/api/states/all?"
        self.aeroplanes = None

    def get_coordinates(self, country: str) -> None:
        country_checked = pycountry.countries.get(name=country)
        if country_checked is None:
            raise ValueError("Неправильно введено название страны")
        else:
            country_checked = country_checked.name
        headers_nominatim = {
            "User-Agent": "test-app/1.0",
        }

        # Указываем параметры: в каком формате возвращать данные и максимальную длину списка стран в ответе.
        params_nominatim = {
            "country": country_checked,
            "format": "json",
            "limit": 1,
        }

        response = requests.get(url=self.openstreetmap_url, params=params_nominatim, headers=headers_nominatim)
        if response.status_code != 200:
            raise ConnectionError("Ошибка в получении данных")
        else:
            data = response.json()

            geo_coordinates = data[0].get("boundingbox")
            self.get_aeroplanes(geo_coordinates)

    def get_aeroplanes(self, geo_coordinates):
        params = {
            "lamin": geo_coordinates[0],
            "lamax": geo_coordinates[1],
            "lomin": geo_coordinates[2],
            "lomax": geo_coordinates[3],
        }

        response = requests.get(url=self.opensky_url, params=params)
        if response.status_code != 200:
            raise ConnectionError("Ошибка в получении данных")
        else:
            self.aeroplanes = response.json().get("states")
