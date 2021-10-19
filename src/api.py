from flask import Flask
from flask_restful import Resource, Api
from tasks import add as task_add
from tasks import pronoun_counter as task_counter

app = Flask(__name__)
api = Api(app)

class Count(Resource):
    def get(self):
        result = task_counter('data')
        return result

api.add_resource(Count, '/')

if __name__ == '__main__':
    app.run(debug=True)