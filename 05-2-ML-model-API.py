import pickle
from flask import Flask
from flask_restful import Api, Resource
from flask_jsonpify import jsonify  # it seems we don't need flask_jsonpify

app = Flask(__name__)
api = Api(app)


class LM(Resource):
    def get(self, x1, x2):
        lm = pickle.load(open('05_model.pkl', 'rb'))
        y = lm.predict([[x1, x2]])[0]

        # Careful! Returning the tuple of jsonify() and the HTTP status (200)
        # like before won't work here (why tho?).
        return jsonify(y=y, x1=x1, x2=x2)


api.add_resource(LM, "/predict/<int:x1>/<int:x2>")
app.run(port=5005, debug=True)
