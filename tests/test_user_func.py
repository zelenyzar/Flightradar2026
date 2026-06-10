from unittest.mock import patch

import pytest

from src.class_api import Aircrafts
from src.information import AircraftInfo
from src.user_func import filter_aeroplanes, get_aeroplanes_by_altitude, get_top_aeroplanes


@patch("requests.get")
def test_get_aeroplanes_by_altitude(mock_get, aeroplanes):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value.get.return_value = aeroplanes
    aircraft = Aircrafts()
    aircraft.get_coordinates("Canada")
    aircraft_list = AircraftInfo.list_aeroplanes(aircraft)
    assert get_aeroplanes_by_altitude(aircraft_list, "1000 - 1500")[0].geo_altitude == 1242.06
    with pytest.raises(ValueError):
        get_aeroplanes_by_altitude(aircraft_list, "tkhm")


@patch("requests.get")
def test_filter_aeroplanes(mock_get, aeroplanes):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value.get.return_value = aeroplanes
    aircraft = Aircrafts()
    aircraft.get_coordinates("Canada")
    aircraft_list = AircraftInfo.list_aeroplanes(aircraft)
    assert filter_aeroplanes(aircraft_list, "Canada")


@patch("requests.get")
def test_get_top_aeroplanes(mock_get, aeroplanes):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value.get.return_value = aeroplanes
    aircraft = Aircrafts()
    aircraft.get_coordinates("Canada")
    aircraft_list = AircraftInfo.list_aeroplanes(aircraft)
    assert get_top_aeroplanes(aircraft_list, 2)[0].geo_altitude == 3421.38
