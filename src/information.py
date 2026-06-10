import pycountry


class AircraftInfo:
    """класс, который содержит информацию по самолетам"""

    def __init__(self, callsign, velocity, country, geo_altitude, spi):
        self.callsign = self.valid_str(callsign)
        self.velocity = self.valid_float(velocity)
        self.country = self.valid_country(country)
        self.geo_altitude = self.valid_float(geo_altitude)
        self.spi = self.valid_boolean(spi)

    def __ge__(self, other):
        """метод сравнения высоты"""
        return self.geo_altitude >= other.geo_altitude

    def __le__(self, other):
        """метод сравнения скорости"""
        return self.velocity <= other.velocity

    @staticmethod
    def valid_str(string):
        """проверка строчных атрибутов"""
        if not isinstance(string, str):
            raise ValueError("Передано неверное значение")
        else:
            return string

    @staticmethod
    def valid_float(num):
        """проверка числовых атрибутов"""
        if not isinstance(num, float | int):
            num = 0
        return num

    @staticmethod
    def valid_country(string):
        """проверка правильности указания страны"""
        if not isinstance(string, str):
            raise ValueError("Передано неверное значение")
        else:
            country_valid = pycountry.countries.get(name=string)
            if country_valid is None:
                raise ValueError("Такой страны нет")
            else:
                country_valid = country_valid.name
            return country_valid

    @staticmethod
    def valid_boolean(boolean):
        """проверка булевых атрибутов"""
        if not isinstance(boolean, bool):
            raise ValueError("Передано неверное значение")
        else:
            return boolean

    @staticmethod
    def list_aeroplanes(aeroplanes):
        craft_list = []
        for aeroplane in aeroplanes.aeroplanes:
            try:
                aeroplane_info = AircraftInfo(aeroplane[1], aeroplane[9], aeroplane[2], aeroplane[13], aeroplane[15])
                craft_list.append(aeroplane_info)
            except ValueError:
                pass
        return craft_list
