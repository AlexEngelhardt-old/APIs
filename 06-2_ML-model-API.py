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
from keras import backend as K


app = Flask("api05")
api = Api(app)


class Suggester(Resource):
    def get(self, n=1):
        gen = sng.Generator.load('model')
        names = gen.simulate(n=5)

        # If you don't clear_session, the model will get confused and raise
        # an error:
        # https://github.com/tensorflow/tensorflow/issues/14356#issuecomment-389606499
        K.clear_session()

        return jsonify(names)


api.add_resource(Suggester, '/suggest')

app.run(port='5006')
