from flask import Flask
from config import Configuration

from news.view import news


app = Flask(__name__)

app.register_blueprint(news, url_prefix='/news')
app.config.from_object(Configuration)
