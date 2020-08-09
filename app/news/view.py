from flask import render_template, abort
from flask import Blueprint
from jinja2 import TemplateNotFound


news = Blueprint('news', __name__, 
				template_folder='templates', 
				static_folder='static')

@news.route('/')
def index():
	try:
		return render_template('news/index.html')
	except TemplateNotFound:
		abort(404)