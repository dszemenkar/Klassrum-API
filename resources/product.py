from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.product import ProductModel

class Product(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('desc_short',
		type=str,
		required=True,
		help="This field cannot be left blank!")
	parser.add_argument('desc_long',
		type=str,
		required=True,
		help="Hey! You forgot english, mate!")
	parser.add_argument('pdf',
		type=str,
		required=True,
		help="Achtung! What about german?")
	parser.add_argument('price_excl',
		type=float,
		required=True,
		help="Every product needs a latitude!")
	parser.add_argument('price_incl',
		type=float,
		required=True,
		help="Every product needs a longitude!")

	parser.add_argument('store_id',
		type=int,
		required=True,
		help="Every product needs a store.")

	def get(self, name):
		product = ProductModel.find_by_name(name)
		if product:
			return product.json()
		return {'message': 'product not found'}, 404


	#@jwt_required()
	def post(self, name):
		if ProductModel.find_by_name(name):
			return {'message': "A product with name '{}' already exists.".format(name)}, 400

		data = product.parser.parse_args()
		product = ProductModel(name, **data)

		try:
			product.save_to_db()
		except:
			return {'message': 'An error occured inserting the product'}, 500

		return product.json(), 201

	def delete(self, name):
		product = ProductModel.find_by_name(product)
		if product:
			product.delete_from_db()

	def put(self, name):
		data = product.parser.parse_args()

		product = ProductModel.find_by_name(name)

		if product is None:
			product = ProductModel(name, **data)
		else:
			product.desc_short = data['desc_short']
			product.desc_long = data['desc_long']
			product.pdf = data['pdf']
			product.price_excl = data['price_excl']
			product.price_incl = data['price_incl']

		product.save_to_db()
		return product.json()


class productList(Resource):
	def get(self):
		return {'products': [product.json() for product in ProductModel.query.all()]}