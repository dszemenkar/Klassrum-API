import os

from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT

from security import authenticate, identify
from resources.user import UserRegister
from resources.product import Product, ProductList
from resources.store import Store, StoreList
from resources.image import Image

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'david'
api = Api(app)

jwt = JWT(app, authenticate, identify)

api.add_resource(store, '/stores/<string:name>')
api.add_resource(Product, '/products/<string:name>')
api.add_resource(ProductList, '/products')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(Image, '/images')

if __name__ == '__main__':
	db.init_app(app)
	app.run(port=5000, debug=True)


