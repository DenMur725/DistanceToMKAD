import pytest
from flask import Flask
from os import path, makedirs, getcwd
from ..geo.geo import geo

@pytest.fixture()
def app():
    """Creating a test server."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key_for_flashed_messages'
    app.register_blueprint(geo, url_prefix='/geo')
    yield app

@pytest.fixture()
def client(app):
    """Creating a test client."""
    return app.test_client()

@pytest.fixture()
def filepath():
    """Location of test log files."""
    filepath = getcwd() + '\\tests\\test_log\\'
    if not path.isdir(filepath):
        makedirs(filepath)
    yield filepath
