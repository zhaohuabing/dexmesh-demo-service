import os
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

class Version(Resource):
    def get(self):
        return {'version': os.environ["VERSION"]} 

api.add_resource(Version, '/api/dexmeshdemo/v1/appversion') # Route_1


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='1313')
