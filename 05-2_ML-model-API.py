"""This script hosts an API for a machine learning
model. It will serve company name suggestions via HTTP!

First create a SNG model by running `05_create-ML-model.py`. This will
store the `model.pkl` file on your disk. This script here then loads and
hosts this model.
"""

import sng
from flask import Flask
from flask_restful import Resource, Api
from flask_jsonpify import jsonify


app = Flask("api05")
api = Api(app)

gen = sng.Generator.load('model')


class Suggester(Resource):
    def get(self):
        name = gen.simulate(n=1)[0]
        return jsonify(name)


api.add_resource(Suggester, '/suggest')

app.run(port='5005')


