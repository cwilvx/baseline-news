from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_headlines,get_everything

@main.route('/')
def index():
	sources = get_sources()
	everything = get_everything()
	print(sources)
	title = 'News Highlight'
	return render_template('index.html',title = title,sources = sources,everything = everything)

@main.route('/source/<source>')
def Headlines(source):
	sources = get_sources()
	Headlines = get_headlines(source)
	print(Headlines)

	return render_template('headlines.html',sources = sources,Headlines = Headlines)