import pytest
from os import path, getcwd, remove
from ..geo.settings import NAME_LOG_FILE

def delete_test_log_data():
    """Deleting text log-data from the default log-file."""
    file = getcwd() + '\\' + NAME_LOG_FILE
    data_old = ''
    with open(file, "r") as f:
        data = f.readlines()
        data.pop()
        data_old = ''.join(data)
    if data_old == '':
        remove(file)
    else:
        with open(file, 'w') as f:
            f.write(data_old)

def test_geo_success_get(client):
    """Simple page loading."""
    response = client.get("/geo/")
    assert 200 == response.status_code

@pytest.mark.parametrize("suggest", [("Nizhny Novgorod"),
                                     ("NiNo"),
                                     ("NN")
                                     ])
def test_geo_success_post(client, suggest):
    """Sending a correct post request with the correct address."""
    response = client.post("/geo/", data={"suggest" : suggest})
    assert 200 == response.status_code
    delete_test_log_data()

@pytest.mark.parametrize("suggest", [("NNNNNNNNN"),
                                     ("T9y5465UT67"),
                                     ("")
                                     ])
def test_geo_bad_addres(client, suggest):
    """Sending a correct post request with the incorrect address."""
    response = client.post("/geo/", data={"suggest" : suggest})
    assert 200 == response.status_code

def test_geo_bad_request(client):
    """Sending a incorrect post request."""
    response = client.post("/geo/", data={"suggest111" : "Nizhny Novgorod"})
    assert 400 == response.status_code

def test_geo_not_found(client):
    """Incorrect page."""
    response = client.post("/geo111/", data={"suggest" : "Nizhny Novgorod"})
    assert 404 == response.status_code
