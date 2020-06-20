# News-Highlight

News Highlight is a python web app made using flask framework. The app consumes the [News Api](https://newsapi.org/). It queries news from  54 different countries, 14 different languages,7 categories and 128 different news providers and shows to the user.

| Behavior- the program should handle: | Input Example- When it receives: | Output Example- It should return: |
| :-------------: | :-------------: | :-------------: |
| User Sort Preference | Category,countries,sources | News from each category |
| Show user articles from a single source | Click Source name on Source page |Redirect to the full article's website |
| Enable user to continue reading an article | Click news title | Redirect to that article |

# Installation
* Clone Project
* Navigate to the root folder of the app
* Activate a virtual environment
* Install all the dependencies needed. Look at requirements.txt
* Sign up at [newsapi.org](newsapi.org) and get your apiKey
* Fill the ```start.sh``` file with your API_KEY and desired SECRET_KEY
* Make ```start.sh``` excecutable
* Access the live site using the local host provided
* Or access the hosted website by clicking [here](https://iamcwilv-news-highlights.herokuapp.com/)

```sh
$ git clone git@github.com:geoffrey45/News-highlight.git
$ cd News-highlight
$ . virtual/bin/activate
$ pip install -r requirements.txt
$ chmod a+x start.sh
$ ./start.sh
```
## Known Bugs

* 404 page not available right now
* returning no results in search gives a nonetype error
* database not linked in live version

## Tools Used
* Python3.6.
* Flask
* CSS for styling.
* HTML for webpage design.

## Support and contact details

geoffreymungai45@gmail.com

License
----
MIT

