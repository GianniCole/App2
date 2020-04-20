import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)
RSS_FEEDS = {'bbc': "http://feeds.bbci.co.uk/news/rss.xml",
            'cnn': 'http://rss.cnn.com/rss/edition.rss',
            'fox':'http://feeds.foxnews.com/foxnews/latest',
            'iol': 'http://www.iol.co.za/cmlink/1.640'}

@app.route("/")


  
@app.route("/<pubblication>")
def get_news(pubblication="bbc"):
    feed = feedparser.parse(RSS_FEEDS[pubblication])
    first_article = feed['entries'][0]
    #passing dunamic data to my tempalte
    return render_template("index.html", articles=feed['entries'])
if __name__ == "__main__":
    app.run(port=5000, debug=True)