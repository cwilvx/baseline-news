from flask import render_template
from . import main

@main.app_errorhandler(404)
def fof(error):
	return render_template('fof.html'),404