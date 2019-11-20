from flask import Flask
from flask_restful import Resource, Api
import redis
import json

app = Flask(__name__)
api = Api(app)

r = redis.Redis(host="redis-service", port=6379)


class Product(Resource):
    def get(self):
        keys = r.keys()
        data = []
        for key in keys:
            if key.decode('utf-8').__contains__("product_"):
                data.append(r.get(key).decode('utf-8'))
        return data


api.add_resource(Product, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
