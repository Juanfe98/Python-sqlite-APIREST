from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

# Here we define a Resource that return a student


class Student(Resource):
    def get(self, name):
        return {'student': name}


# Configuration to access the Student Resource
# http://127.0.0.1:5000/student/Juan
api.add_resource(Student, '/student/<string:name>')


class Item(Resource):
    def get(self, name):
        # lambda function to retrieve the item from the database
        item = next(filter(lambda x: x.name == name, items), None)
        # Terniary operator
        return {item: item}, 200 if item else 404

    def post(self, name):
        # We validate if the item exists
        if next(filter(lambda x: x.name == name, items), None):
            return {"message": "An item with name '{}' already exists.".format(name)}, 400
        # Getting the data from the body
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class ItemsList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemsList, '/items')


app.run(port=5000, debug=True)

# HTTP status code
# 201 Created
# 400 Bad Request
# 404 Not Found
# 202 Accepted, could take long to create item
