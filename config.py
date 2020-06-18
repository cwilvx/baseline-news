import os

class Config:
	SOURCES_URL = 'https://newsapi.org/v2/sources?apiKey={}'
	HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apikey={}'
	EVERYTHING_URL = 'https://newsapi.org/v2/everything?q=android&language=en&apiKey={}'
	SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://cwilv:iamcwilv@localhost/__news'

	SQLALCHEMY_TRACK_MODIFICATIONS = True
	API_KEY = os.environ.get('API_KEY')
	SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
	pass

class TestConfig(Config):
	pass

class DevConfig(Config):
	DEBUG = True

config_options = {
	'development': DevConfig,
	'test':TestConfig,
	'production':ProdConfig
}