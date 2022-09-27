# Denis Muravev
from flask import Blueprint, request, render_template, flash
from yandex_geocoder import Client, exceptions
from .logging_data import logging
from .settings import API_KEY, API_SRC

geo = Blueprint('geo', __name__, template_folder='templates')

@geo.route('/', methods=["POST", "GET"])
def geo_page():
    if request.method == "POST":
        client = Client(API_KEY)
        addres = request.form['suggest']
        try:
            coordinates = client.coordinates(addres)
            coordinates = [float(coordinates[1]), float(coordinates[0])] # [Latitude, Longitude]
            log_data = logging(coordinates, addres)
            if log_data == None:
                flash("Warning: The address is located inside the MKAD, no record has been made")
            else:
                flash("Success: Data recorded")
                flash(log_data)
        except exceptions.NothingFound:
            flash("Error: NothingFound")
        except exceptions.UnexpectedResponse:
            flash("Error: UnexpectedResponse")
    return render_template("geo/geo.html", apisrc=API_SRC)
