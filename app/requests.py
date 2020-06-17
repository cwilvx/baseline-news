import urllib.request, json
from .models import Sources,Headlines,Everything

api_key = None
sources_url = None
headlines_url = None
everything_url = None

def configure_request(app):
	global api_key,sources_url,headlines_url,everything_url
	api_key = app.config["API_KEY"]
	sources_url = app.config["SOURCES_URL"]
	headlines_url = app.config["HEADLINES_URL"]
	everything_url = app.config["EVERYTHING_URL"]

def get_sources():
	get_sources_url = sources_url.format(api_key)

	with urllib.request.urlopen(get_sources_url) as url:
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)

		sources_results = None

		if get_sources_response['sources']:
			sources_results_list = get_sources_response['sources']
			sources_results = process_sources_results(sources_results_list)
	return sources_results

def process_sources_results(sources_results_list):
	sources_results = []
	for source_item in sources_results_list:
		id = source_item.get('id')
		name = source_item.get('name')
		description = source_item.get('description')
		url = source_item.get('url')
		category = source_item.get('category')
		language = source_item.get('language')
		country = source_item.get('country')

		source_object = Sources(id,name,description,url,category,language,country)
		sources_results.append(source_object)

	return sources_results

def get_headlines(source):
	get_headlines_url = headlines_url.format(source,api_key)

	with urllib.request.urlopen(get_headlines_url) as url:
		headlines_data = url.read()
		headlines_response = json.loads(headlines_data)
		headlines_results = None

		if headlines_response['articles']:
			headlines_results_list = headlines_response['articles']
			headlines_results = process_headlines_results(headlines_results_list)

	return headlines_results

def process_headlines_results(headlines_results_list):
	headlines_results = []
	for headline_item in headlines_results_list:
		author = headline_item.get('author')
		title = headline_item.get('title')
		description = headline_item.get('description')
		url = headline_item.get('url')
		urlToImage = headline_item.get('urlToImage')
		publishedAt = headline_item.get('publishedAt')
		content = headline_item.get('content')
		
		headlines_object = Headlines(author,title,description,url,urlToImage,publishedAt,content)
		headlines_results.append(headlines_object)

	return headlines_results

def get_everything():
	get_everything_url = everything_url.format(api_key)
	with urllib.request.urlopen(get_everything_url) as url:
		get_everything_data = url.read()
		get_everything_response = json.loads(get_everything_data)

		everything_results = None

		if get_everything_response['articles']:
			everything_results_list = get_everything_response['articles']
			everything_results = process_everything_results(everything_results_list)

	return everything_results

def process_everything_results(everything_results_list):
	everything_results = []
	for everything_item in everything_results_list:
		author = everything_item.get('author')
		title = everything_item.get('title')
		description = everything_item.get('description')
		url = everything_item.get('url')
		urlToImage = everything_item.get('urlToImage')
		publishedAt = everything_item.get('publishedAt')
		content = everything_item.get('content')
		totalResults = everything_item.get('totalResults')

		everything_object = Everything(author,title,description,url,urlToImage,publishedAt,content,totalResults)
		everything_results.append(everything_object)
	
	return everything_results

def search_news(keyword):
	search_news_url = 'https://newsapi.org/v2/everything?q={}&language=en&apiKey={}'.format(keyword,api_key)
	with urllib.request.urlopen(search_news_url) as url:
		search_news_data = url.read()
		search_news_response = json.loads(search_news_data)

		search_news_results = None

		if search_news_response['articles']:
			search_news_list = search_news_response['articles']
			search_news_results = process_search_results(search_news_list)

	return search_news_results

def process_search_results(search_news_list):
	news_results = []
	for search_results_item in search_news_list:
		author = search_results_item.get('author')
		title = search_results_item.get('title')
		description = search_results_item.get('description')
		url = search_results_item.get('url')
		urlToImage = search_results_item.get('urlToImage')
		publishedAt = search_results_item.get('publishedAt')
		content = search_results_item.get('content')
		totalResults = search_results_item.get('totalResults')

		if content:
			news_results_object = Everything(author,title,description,url,urlToImage,publishedAt,content,totalResults)
			news_results.append(news_results_object)
	return news_results