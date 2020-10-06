from flask_restful import Resource, reqparse
from models.image import ImageModel

class Image(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('url',
		type=str,
		required=True,
		help="This field cannot be left blank!")

	parser.add_argument('product_id',
		type=int,
		required=True,
		help="Every image needs a product.")

	def get(self, place_id):
		image = ImageModel.find_by_place(product_id)
		if image:
			return image.json()
		return {'message': 'image not found'}, 404

	def post(self):
		data = Image.parser.parse_args()

		image = ImageModel(**data)
		try:
			image.save_to_db()
		except:
			return {'message': "An error occured creating the image."}, 500
		return image.json(), 201

	def delete(self, _id):
		image = ImageModel.find_by_id(_id)
		if image:
			image.delete_from_db()
			return {'message': 'Image has been deleted.'}


class ImageList(Resource):
	def get(self):
		return {'images': [image.json() for image in ImageModel.query.all()]}