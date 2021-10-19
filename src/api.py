from flask import Flask
from flask_restful import Resource, Api
from tasks import add as task_add

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class AddNumbers(Resource):
    def get(self):
        result = task_add.delay(4, 4)
        return result.get()

api.add_resource(HelloWorld, '/')
api.add_resource(AddNumbers, '/add')

if __name__ == '__main__':
    app.run(debug=True)