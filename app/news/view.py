from flask import render_template, abort
from flask import Blueprint
from jinja2 import TemplateNotFound

from models import Post


news = Blueprint('news', __name__, 
				template_folder='templates', 
				static_folder='static')

@news.route('/')
def index():
	try:
		posts = Post.query.order_by(Post.created.desc()).limit(8)

		return render_template('news/index.html',posts=posts)
	except TemplateNotFound:
		abort(404)