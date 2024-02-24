"""This is a web app that helps users get news summaries from different newspapers"""
from flask import Flask, render_template
import feedparser

app = Flask(__name__)

# A dictionary of the RSS Feeds
RSS_FEEDS = {
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'guardian': 'http://www.guardian.ng/feed/'
    }

@app.route('/')
@app.route('/home')
def index():
	"""Returns the home page of the web app"""
	return render_template("home.html")

@app.route('/select')
def select():
	"""Returns the web page to select newspaper to see"""
	return render_template("select.html")

@app.route('/<news>')
def get_news(news):
	"""Returns the news article"""
	feed = feedparser.parse(RSS_FEEDS[news])
	the_article = feed['entries']
	return render_template("news.html", articles=the_article)

if __name__ == "__main__":
	app.run(debug=True, port=5000)