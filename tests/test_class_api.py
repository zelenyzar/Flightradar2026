from unittest.mock import patch

import pytest

from src.class_api import Aircrafts


@patch("requests.get")
def test_get_aeroplanes(mock_get, aeroplanes, aeroplanes_2):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value.get.return_value = aeroplanes
    aircraft = Aircrafts()
    aircraft.get_coordinates("Canada")
    assert aircraft.aeroplanes[0] == aeroplanes_2


@patch("requests.get")
def test_get_aeroplanes_1(mock_request):
    mock_request.return_value.status_code = 400
    aircraft = Aircrafts()
    with pytest.raises(ConnectionError):
        aircraft.get_coordinates("Canada")
    with pytest.raises(ConnectionError):
        aircraft.get_aeroplanes([0, 1, 2, 3])
    with pytest.raises(ValueError):
        aircraft.get_coordinates("123")
