import json
from abc import ABC, abstractmethod
from json import JSONDecodeError

from config import DIR_PATH
from src.information import AircraftInfo


class FileWork(ABC):
    """абстрактный класс, определяющий методы по работе с файлом, который содержит информацию о самолете"""

    @abstractmethod
    def add_info(self, aircraft: AircraftInfo) -> None:
        pass

    @abstractmethod
    def read_info(self) -> None:
        pass

    @abstractmethod
    def delete_info(self, aircraft: AircraftInfo) -> None:
        pass


class SaveInfoAircraft(FileWork):
    """класс для сохранения информации о самолетах"""

    def __init__(self, filename):
        self.filename = self.valid_str(filename)

    @staticmethod
    def valid_str(string):
        if string == "":
            return DIR_PATH + "/data/aircraft_info.json"
        else:
            return string

    def add_info(self, aircraft: AircraftInfo) -> None:
        with open(self.filename, "a+", encoding="UTF-8") as f:
            f.seek(0)
            try:
                data = json.load(f)
            except JSONDecodeError:
                data = []
            air = {
                "callsign": aircraft.callsign,
                "velocity": aircraft.velocity,
                "country": aircraft.country,
                "geo_altitude": aircraft.geo_altitude,
                "spi": aircraft.spi,
            }
            if air not in data:
                data.append(air)
                f.seek(0)
                f.truncate()
                json.dump(data, f, ensure_ascii=False, indent=4)
                print("Информация добавлена в файл")
            else:
                print("Данная информация уже есть в файле")

    def read_info(self) -> None:
        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    def delete_info(self, aircraft: AircraftInfo) -> None:
        with open(self.filename, "a+", encoding="utf-8") as f:
            f.seek(0)
            try:
                data = json.load(f)
            except JSONDecodeError:
                data = []
            air = {
                "callsign": aircraft.callsign,
                "velocity": aircraft.velocity,
                "country": aircraft.country,
                "geo_altitude": aircraft.geo_altitude,
                "spi": aircraft.spi,
            }
            data_new = []
            if air in data:
                for airplane in data:
                    if airplane != air:
                        data_new.append(airplane)
                print("Информация удалена")
            else:
                data_new = data
                print("Информация отсутствует в файле")
            f.seek(0)
            f.truncate()
            json.dump(data_new, f, ensure_ascii=False, indent=4)
            print("ok")
