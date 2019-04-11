"""This API returns a list of people defined in an external CSV file

Adapted and simplified (a lot) from:
https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq
"""

from flask import Flask
from flask_restful import Resource, Api
from flask_jsonpify import jsonify

import pandas as pd


app = Flask("mysecondapi")
api = Api(app)


class People(Resource):
    def get(self):
        guys = pd.read_csv('02_serve-data.csv')
        # .to_json() returns a string instead of a JSON object. We have to
        # use jsonify(). This does not work outside of a Flask application
        # context.
        return jsonify(guys.to_dict())


api.add_resource(People, '/people')

app.run(port='5002')
