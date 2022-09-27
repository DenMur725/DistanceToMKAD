import pytest
from ..geo.logging_data import not_inside

@pytest.mark.parametrize("point, polygon", [((20, 20), ((0, 0), (10, 0), (10, 10))),
                                            ((11, 11), ((0, 0), (10, 0), (10, 10), (0, 10))),
                                            ((30, -30), ((0, 0), (10, 0), (10, 10), (0, 10))),
                                            ])
def test_not_inside_true(point, polygon):
    """The point is outside the polygon"""
    assert True == not_inside(point, polygon)

@pytest.mark.parametrize("point, polygon", [((9, 1), ((0, 0), (10, 0), (10, 10))),
                                            ((0, 5), ((0, 0), (10, 0), (10, 10), (0, 10))),
                                            ((0, 0), ((0, 0), (10, 0), (10, 10), (0, 10))),
                                            ])
def test_not_inside_false(point, polygon):
    """The point is inside the polygon"""
    assert False == not_inside(point, polygon)

@pytest.mark.parametrize("point, polygon", [((91, 181), ((0, 0), (10, 0), (10, 10))),
                                            ((-91, 0), ((0, 0), (10, 0), (10, 10), (0, 10))),
                                            ((0, 0), ((1000, 0), (10, 0), (10, 10), (0, 10))),
                                            ])
def test_not_inside_error(point, polygon):
    """Incorrect data, stopping work."""
    assert None == not_inside(point, polygon)