# Baseline News

Baseline News is a python web app made using flask (a python framework). The app consumes a [News Api](https://newsapi.org/). It queries News from  54 different countries, 14 different languages,7 categories and 128 different news providers and shows to the user on demand.

# Installation
* Clone Project
* Navigate to the root folder of the app
* Add and activate a virtual environment
* Install all the dependencies needed.
* Sign up at [newsapi.org](newsapi.org) and get your apiKey
* Fill the ```start.sh``` file with your API_KEY and desired SECRET_KEY
* Make ```start.sh``` excecutable
* Access the live site using the local host provided
* Or access the site by clicking [here](https://baselinenews.herokuapp.com/)

```sh
$ git clone git@github.com:geoffrey45/Baseline-news.git
$ cd News-highlight
$ . virtual/bin/activate
$ pip install -r requirements.txt
$ chmod a+x start.sh
$ ./start.sh
```
## Known Bugs

* Don't search unexisting word

## Tools Used
* Python3.6.
* Flask 1.12
* HTML5

## Support and contact details

geoffreymungai45@gmail.com

License
----
MIT

