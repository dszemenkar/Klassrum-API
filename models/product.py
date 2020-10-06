from db import db

class ProductModel(db.Model):
	__tablename__ = 'products'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	desc_short = db.Column(db.String(1000))
	desc_long = db.Column(db.String(3000))
	pdf = db.Column(db.String(150))
	price_excl = db.Column(db.Float(precision=2))
	price_incl = db.Column(db.Float(precision=2))

	images = db.relationship('ImageModel', lazy='dynamic')

	store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
	store = db.relationship('StoreModel')


	def __init__(self, name, desc_short, desc_long, pdf, price_excl, price_incl, store_id):
		self.name = name
		self.desc_short = desc_short
		self.desc_long = desc_long
		self.pdf = pdf
		self.price_excl = price_excl
		self.price_incl = price_incl
		self.store_id = store_id

	def json(self):
		return {'name': self.name, 'desc_short': self.desc_short, 'desc_long': self.desc_long, 'pdf': self.pdf, 'price_excl': self.price_excl, 'price_incl': self.price_incl, 'images': [image.json() for image in self.images.all()]}

	@classmethod
	def find_by_name(cls, name):
		return cls.query.filter_by(name=name).first()

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()