"""The most simple API ever. It returns four.

Run it with `python 01_simple-flask-API.py` in your console, then
leave it running and enter "localhost:5001/four" in your browser or
via wget or curl.
You will see a JSON document containing the number four.

Adapted and simplified (a lot) from:
https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq
"""

from flask import Flask
from flask_restful import Resource, Api


app = Flask("myfirstapi")
api = Api(app)


class Four(Resource):
    def get(self):
        return 4


api.add_resource(Four, '/four')

app.run(port='5001')
