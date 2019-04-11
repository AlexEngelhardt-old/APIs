""" An API that exposes GET, PUT, POST, and DELETE endpoints

Request some user by calling:

curl http://localhost:5003/user/Alice

You can use `curl` to send a POST request by e.g. calling:

curl --header "Content-Type: application/json" \
     -d '{"name": "Derp", "age": 33, "job": "Top Derper"}' \
     http://localhost:5003/user/Derp

Now you can query Derp:

curl http://localhost:5003/user/Derp

Derp will be lost when the server restarts, of course. In reality, we'd
use a database.

To PUT or DELETE, use curl's --request parameter:

curl --request "DELETE" http://localhost:5003/user/Alice
curl http://localhost:5003/user/Alice  # will be gone now

Update a guy with:

curl --request "PUT" --header "Content-Type: application/json" -d '{"age": 32, "job": "fired"}' http://localhost:5003/user/Bob
curl http://localhost:5003/user/Bob  # will be updated now


Btw: You can also look at the HTTP Response code by passing the '-v' argument
to curl. This will show a verbose output.

Adapted from:
https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3
"""

from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask('app03')
api = Api(app)

users = [
    {
        "name": "Alice",
        "age": 52,
        "job": "Just sits there"
    },
    {
        "name": "Bob",
        "age": 32,
        "job": "Food Guy"
    },
    {
        "name": "Carol",
        "age": 45,
        "job": "Types stuff"
    },
]


class User(Resource):
    def get(self, name):
        """Retreive one user"""
        for user in users:
            if name == user['name']:
                return user, 200
        return "User not found!", 404

    def post(self, name):
        """Create a new user"""
        parser = reqparse.RequestParser()
        parser.add_argument('age')
        parser.add_argument('job')
        args = parser.parse_args()  # how does he know about 'name'?

        for user in users:
            if name == user['name']:
                return "User {} already exists".format(name), 400

        user = {
            'name': name,
            'age': args['age'],
            'job': args['job'],
        }

        users.append(user)
        return user, 201

    def put(self, name):
        """Update an existing user, *or* create new user if not exists"""
        parser = reqparse.RequestParser()
        parser.add_argument('age')
        parser.add_argument('job')
        args = parser.parse_args()

        global users  # need this so the properties get updated outside too
        for user in users:
            if name == user['name']:
                user['age'] = args['age']
                user['job'] = args['job']
                return user, 200

        # else: he's a new user

        user = {
            'name': name,
            'age': args['age'],
            'job': args['job'],
        }
        users.append(user)
        return user, 201  # notice the different return code (201 created)

    def delete(self, name):
        """Delete a user from the "database" """
        global users
        # ugh wtf. this is not a pretty way to solve this, but I'm just
        # following the tutorial here.
        users = [user for user in users if user['name'] != name]
        return "{} is deleted.".format(name), 200


api.add_resource(User, "/user/<string:name>")
app.run(port=5003, debug=True)
