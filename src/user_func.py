def get_top_aeroplanes(aircraft_info, top_n, sort_aeroplanes=True):
    """функция сортировки самолетов по высоте (по умолчанию - по убыванию) и
    вывод нужного количества самолетов из этого списка"""
    aircraft_list = sorted(aircraft_info, key=lambda x: x.geo_altitude, reverse=sort_aeroplanes)
    return aircraft_list[:top_n]


def filter_aeroplanes(aircraft_info, filter_words):
    """функция фильтрации самолетов по стране регистрации"""
    aircraft_list = []
    for aircraft in aircraft_info:
        if filter_words == aircraft.country:
            aircraft_list.append(aircraft)
    return aircraft_list


def get_aeroplanes_by_altitude(aircraft_info, altitude_range):
    """функция фильтрации самолетов по диапазону высот"""
    altitude_range = altitude_range.split(" - ")
    if len(altitude_range) != 2:
        raise ValueError("Данные заданы некорректно")
    altitude_range = [int(altitude) for altitude in altitude_range]
    aircraft_list = []
    for aircraft in aircraft_info:
        if altitude_range[0] <= aircraft.geo_altitude <= altitude_range[1]:
            aircraft_list.append(aircraft)
    return aircraft_list
