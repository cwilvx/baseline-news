from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class Sources:
	def __init__(self,id,name,description,url,category,language,country):
		self.id = id
		self.name = name
		self.description = description
		self.url = url
		self.category = category
		self.language = language
		self.country = country

class Headlines:
	def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
		self.author = author
		self.title = title
		self.description = description
		self.url = url
		self.urlToImage = urlToImage
		self.publishedAt = publishedAt
		self.content = content

class Everything:
	def __init__(self,author,title,description,url,urlToImage,publishedAt,content,totalResults):
		self.author = author
		self.title = title
		self.description = description
		self.url = url
		self.urlToImage = urlToImage
		self.publishedAt = publishedAt
		self.content = content
		self.totalResults = totalResults

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String(255))
	users = db.relationship('User',backref = 'role',lazy = "dynamic")

	def __repl__(self):
		return f'User{self.name}'
