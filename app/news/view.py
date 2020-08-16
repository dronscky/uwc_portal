from flask import render_template, abort
from flask import Blueprint
from jinja2 import TemplateNotFound

# from models import Post


news = Blueprint('news', __name__, 
				template_folder='templates', 
				static_folder='static')

@news.route('/')
def index():
	try:
		# создать запрос 6ти последних статей в БД с названием статьи,
		# с куском статьи в 100 символов и пути к изображению
		posts = Post.query.order_by(Post.created.desc()).limit(6)

		return render_template('news/index.html')
	except TemplateNotFound:
		abort(404)