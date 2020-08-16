from datetime import datetime
import random

from app import db


def slugify():
	a = '1234567890abcdefghijklmnopqrstuvwxyz'
	return ''.join(random.sample(a, 6))


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(140))
	body = db.Column(db.Text)
	slug = db.Column(db.String(10), unique=True)
	photo = db.Column(db.String(25))
	created = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, *args, **kwargs):
		super(Post, self).__init__(*args, **kwargs)
		self.slug = slugify()

	def __repr__(self):
		return f'Post {self.title} has {self.slug} slug and created {self.created}'

