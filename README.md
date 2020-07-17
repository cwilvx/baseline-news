# Baseline News

Baseline News is a python web app made using flask (a python framework). The app consumes a [News Api](https://newsapi.org/). It queries News from  54 different countries,7 categories and 128 different news providers and shows to the user on demand.

# Installation
* Clone Project
* Navigate to the root folder of the app
* Add and activate a virtual environment
* Install all the dependencies needed.
* Sign up at [newsapi.org](https://newsapi.org) and get your apiKey
* Fill the ```start.sh``` file with your API_KEY and desired SECRET_KEY
* make executable 'start.sh' and inside put the following lines:
```
export API_KEY=<your_news_api_key>
export SECRET_KEY=<your_desired_secret_key>
python3.6 manage.py server
```
*  make the file executable.

* Make ```start.sh``` excecutable
* Access the live site using the local host provided
* Or access the site by clicking [here](https://baselinenews.herokuapp.com/)

```sh
$ git clone git@github.com:geoffrey45/Baseline-news.git
$ cd Baseline-news
$ . virtual/bin/activate
$ pip install -r requirements.txt
$ chmod a+x start.sh
$ ./start.sh
```
## Known Bugs

* None

## Tools Used
* [Python3.6.9](https://www.python.org/downloads/release/python-369/)
* [Flask 1.12](https://flask.palletsprojects.com/en/)
* [HTML5](https://html5.org/)

## Support and contact details

geoffreymungai45@gmail.com

License
----
MIT

Free Software !!