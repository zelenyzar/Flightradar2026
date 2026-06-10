from unittest.mock import patch

import pytest

from src.class_api import Aircrafts
from src.information import AircraftInfo


@patch("requests.get")
def test_aircraftinfo(mock_get, aeroplanes):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value.get.return_value = aeroplanes
    aircraft = Aircrafts()
    aircraft.get_coordinates("Canada")
    aircraft_list = AircraftInfo.list_aeroplanes(aircraft)
    assert len(aircraft_list) == 4
    assert aircraft_list[0] >= aircraft_list[1]
    assert aircraft_list[0] <= aircraft_list[1]
    with pytest.raises(ValueError):
        test = AircraftInfo(1023, 102, "canada", 123, False)
    test1 = AircraftInfo("mfk", "fndj", "canada", 123, False)
    assert test1.velocity == 0
    with pytest.raises(ValueError):
        test2 = AircraftInfo("mfk", 102, "canida", 123, False)
    with pytest.raises(ValueError):
        test3 = AircraftInfo("mfk", 102, "canada", 123, "vnj")
