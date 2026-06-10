import pytest


@pytest.fixture
def aeroplanes():
    return [
        [
            "c07d20",
            "JZA7967 ",
            "Canada",
            1780599905,
            1780599906,
            -73.9981,
            45.417,
            2011.68,
            False,
            121.93,
            269.52,
            8.45,
            None,
            2072.64,
            None,
            False,
            0,
        ],
        [
            "a34230",
            "EJA309  ",
            "United States",
            1780599905,
            1780599905,
            -87.7715,
            41.7458,
            1173.48,
            False,
            144.69,
            58.97,
            0,
            None,
            1242.06,
            None,
            False,
            0,
        ],
        [
            "a41ef3",
            "N365AV  ",
            "United States",
            1780599905,
            1780599906,
            -76.2611,
            42.7573,
            2987.04,
            False,
            171.69,
            99.66,
            0.33,
            None,
            3108.96,
            "7457",
            False,
            0,
        ],
        [
            "acdfa5",
            "N929AM  ",
            "United States",
            1780599905,
            1780599905,
            -86.28,
            43.4693,
            3299.46,
            False,
            101.38,
            91.45,
            0,
            None,
            3421.38,
            None,
            False,
            0,
        ],
    ]


@pytest.fixture
def aeroplanes_2():
    return [
        "c07d20",
        "JZA7967 ",
        "Canada",
        1780599905,
        1780599906,
        -73.9981,
        45.417,
        2011.68,
        False,
        121.93,
        269.52,
        8.45,
        None,
        2072.64,
        None,
        False,
        0,
    ]


@pytest.fixture
def airplanes_file():
    return [
        {"callsign": "aaa", "country": "Canada", "geo_altitude": 12, "spi": False, "velocity": 11},
        {"callsign": "bbb", "country": "Canada", "geo_altitude": 23, "spi": False, "velocity": 21},
    ]
