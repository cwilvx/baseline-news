from flask import render_template,request,redirect,url_for,send_from_directory,session
from . import main
from ..requests import get_sources,get_headlines,get_everything,search_news
from flask_login import login_required,current_user
from ..models import User
from .forms import UpdateProfile
from ..import db,photos

@main.route('/user/<uname>', methods = ['GET', 'POST'])
def profile(uname):
	user = User.query.filter_by(username = uname).first()

	if User is None:
		abort(404)

	return render_template("profile/profile.html",user = user)

@main.route('/user/<uname>/update/bio',methods = ['GET','POST'])
def update_bio(uname):
	user = User.query.filter_by(username = uname).first()
	if user is None:
		abort(404)
	form = UpdateProfile()
	if form.validate_on_submit():
		user.bio = form.bio.data

		db.session.add(user)
		db.session.commit()
		return redirect(url_for('.profile',uname = user.username))
	return render_template('profile/update.html',form = form)



@main.route('/')
def index():
	everything = get_everything()
	title = 'Zorin News Highlight'
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

@main.route('/user/<uname>/update/pic',methods = ['POST'])
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
        return redirect(url_for('main.profile',uname = uname))
