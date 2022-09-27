# Denis Muravev
from flask import Flask, render_template
from geo.geo import geo
from geo.settings import API_SRC

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_for_flashed_messages'

app.register_blueprint(geo, url_prefix='/geo')

@app.route('/')
def main_page():
    """Start page"""
    return render_template("main.html", apisrc=API_SRC)

if __name__ == "__main__":
    app.run()
