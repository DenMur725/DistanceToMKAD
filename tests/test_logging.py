import pytest
from os import path, remove
from ..geo.logging_data import logging


@pytest.mark.parametrize("coordinates, address, result", [((56.326797, 44.006516), "Nizhny Novgorod", "388.157 km to Nizhny Novgorod\n"),
                                                          ((56.326797, 44.006516), "NiNo", "388.157 km to NiNo\n")
                                                          ])
def test_logging_success(filepath, coordinates, address, result):
    """Logging data to a test file and deleting it."""
    file = filepath + "test_log_success.log"
    if path.isfile(file):
        remove(file)
    log_data = logging(coordinates, address, file)
    file_data = ""
    with open(file, "r") as f:
        file_data = f.read()
    assert result == file_data
    assert result == log_data
    remove(file)

@pytest.mark.parametrize("coordinates, address", [((-91, 0), "Nizhny Novgorod"),
                                                  ((0, 181), "NiNo")
                                                  ])
def test_logging_not_file(filepath, coordinates, address):
    """Incorrect data (coordinates). The file is not created."""
    file = filepath + "test_log_not_file.log"
    log_data = logging(coordinates, address, file)
    assert False == path.isfile(file)
    assert None == log_data

@pytest.mark.parametrize("coordinates, address", [((91, 0), "NiNo"),
                                                  ((0, -181), "NN")
                                                  ])
def test_logging_incorrect_data(filepath, coordinates, address):
    """Incorrect data (coordinates). Only one request is logged."""
    file = filepath + "test_log_incorrect_data.log"
    if path.isfile(file):
        remove(file)
    result = "388.157 km to Nizhny Novgorod\n"
    good_log = logging((56.326797, 44.006516), "Nizhny Novgorod", file)
    bad_log = logging(coordinates, address, file)
    data = ""
    with open(file, mode="r") as f:
        data = f.read()
    assert result == data
    assert result == good_log
    assert None == bad_log
    remove(file)
