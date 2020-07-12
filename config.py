import os

class Config:
	SOURCES_URL = 'https://newsapi.org/v2/sources?apiKey={}'
	HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apikey={}'
	EVERYTHING_URL = 'https://newsapi.org/v2/everything?q=android&language=en&apiKey={}'
	SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://cwilv:iamcwilv@localhost/__news'

	SQLALCHEMY_TRACK_MODIFICATIONS = True
	API_KEY = os.environ.get('API_KEY')
	SECRET_KEY = os.environ.get('SECRET_KEY')
	UPLOADED_PHOTOS_DEST = 'app/static/photos'

	basedir = os.path.abspath(os.path.dirname(__name__))
	AVATARS_SAVE_PATH = 'avatars'

class ProdConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
	DEBUG = False

class TestConfig(Config):
	pass

class DevConfig(Config):
	DEBUG = True

config_options = {
	'development': DevConfig,
	'test':TestConfig,
	'production':ProdConfig
}