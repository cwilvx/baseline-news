from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_headlines,get_everything,search_news
from flask_login import login_required,current_user

@main.route('/')
def index():
	everything = get_everything()
	title = 'News Highlight'
	return render_template('index.html',title = title,everything = everything,current_user = current_user)

@main.route('/source/<source>')
def Headlines(source):
	sources = get_sources()
	Headlines = get_headlines(source)
	print(Headlines)

	return render_template('headlines.html',sources = sources,Headlines = Headlines)

@main.route('/sources')
def sources():
	sources = get_sources()
	print(sources)
	return render_template('sources.html',sources = sources)

@main.route('/search/',methods=['GET'])
def search():
	keyword = request.args.get('keyword')
	keyword_list = keyword.split(" ")
	keyword_format = '%20'.join(keyword_list)
	searched_news = search_news(keyword_format)
	title = f'Search results for {keyword} '
	
	return render_template('search.html',searched_news = searched_news)
