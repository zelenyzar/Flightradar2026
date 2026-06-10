from src.class_api import Aircrafts
from src.information import AircraftInfo
from src.user_func import filter_aeroplanes, get_aeroplanes_by_altitude, get_top_aeroplanes


def main():
    try:
        country = input("Введите название страны: \n *Страна указывается латиницей\n")
        aircraft = Aircrafts()
        aircraft.get_coordinates(country)
        aeroplanes = AircraftInfo.list_aeroplanes(aircraft)

        quest1 = input("Отфильтровать по стране регистрации? Да/Нет \n").lower()
        if quest1 == "да":
            filter_words = input(
                "Введите название страны для фильтрации по стране регистрации: \n *Страна указывается латиницей\n"
            )
            filtered_aeroplanes = filter_aeroplanes(aeroplanes, filter_words)

        altitude_range = input("Введите диапазон высот полета: \n Пример: 100000 - 150000\n")
        ranged_aeroplanes = get_aeroplanes_by_altitude(aeroplanes, altitude_range)

        top_n = int(input("Введите количество самолетов для вывода в топ N: \n"))

        top_aeroplanes = get_top_aeroplanes(ranged_aeroplanes, top_n)
        print(f"Топ {top_n} самолетов: ")
        num = 1
        for aeroplane in top_aeroplanes:
            print(f"{num}. Позывной: {aeroplane.callsign}, высота - {aeroplane.geo_altitude}")
            num += 1

    except ValueError as e:
        print(e)
    except ConnectionError as e:
        print(e)
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
