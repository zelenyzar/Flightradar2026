import os

from config import DIR_PATH
from src.class_plane_file import SaveInfoAircraft
from src.information import AircraftInfo


def test_saveinfo(airplanes_file):
    air1 = "aaa", 11, "canada", 12, False
    air2 = "bbb", 21, "canada", 23, False
    file1 = SaveInfoAircraft("")
    file2 = SaveInfoAircraft(DIR_PATH + "/data/test_air.json")
    file2.add_info(AircraftInfo(*air1))
    file2.add_info(AircraftInfo(*air2))
    assert file2.read_info() == airplanes_file
    file2.delete_info(AircraftInfo(*air1))
    assert file2.read_info() == [
        {"callsign": "bbb", "country": "Canada", "geo_altitude": 23, "spi": False, "velocity": 21}
    ]
    os.remove(DIR_PATH + "/data/test_air.json")
    file1.add_info(AircraftInfo(*air1))
    file1.delete_info(AircraftInfo(*air1))
    assert file1.read_info() == []
    os.remove(DIR_PATH + "/data/aircraft_info.json")
