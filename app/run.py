from app import app
from news.view import news

import view


app.register_blueprint(news, url_prefix='/news')

if __name__ == '__main__':
	app.run()
