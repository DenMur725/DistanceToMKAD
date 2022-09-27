import pytest
from ..geo.logging_data import find_min_distance

@pytest.mark.parametrize("polygon, point, result", [(((0, 0), (10, 0), (10, 10), (0, 10)), (0, 0), "0.000"),
                                                    (((0, 0), (10, 0), (10, 10), (0, 10)), (0, 5), "556.597"),
                                                    (((0, 0), (10, 0), (10, 10), (0, 10)), (20, 20), "1541.856"),
                                                    ])
def test_find_min_distance_good(polygon, point, result):
    """Finding the distance to the nearest point of the polygon, with the correct data."""
    assert result == "{:.3f}".format(find_min_distance(point, polygon))

@pytest.mark.parametrize("polygon, point", [(((0, 0), (10, 0), (10, 10), (0, 10)), (1810, 0)),
                                            (((0, 0), (10, 0), (10, 10), (0, 10)), (0, 910)),
                                            (((0, 0), (10, 0), (10, 10), (0, 900)), (20, 20)),
                                            ])
def test_find_min_distance_incorrect_data(polygon, point):
    """Incorrect data, stopping work."""
    assert None == find_min_distance(point, polygon)
