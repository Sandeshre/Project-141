from flask import Flask, jsonify, request
import pandas as pd

articles_data = pd.read_csv('articles.csv')
all_articles = articles_data[['url' , 'title' , 'text' , 'lang' , 'total_events']]
liked_articles = []
not_liked_articles = []

app = Flask(__name__)

def assign_val():
    m_data = {
        "url": all_articles.iloc[0,0],
        "title": all_articles.iloc[0,1],
        "text": all_articles.iloc[0,2] or "N/A",
        "lang": all_articles.iloc[0,3],
        "total_events": all_articles.iloc[0,4]
    }
    return m_data

# API to display first article
@app.route("/get-article")
def get_articles():
    global all_articles
    col = assign_val()
    return jsonify({"data":col,"status":"Success"})


# API to move the article into liked articles list
@app.route("/liked-article")
def liked_article():
        global all_articles,liked_articles
        liked_articles.append(assign_val())
        return jsonify({"data":liked_articles,"status":"Success"})

# # API to move the article into not liked articles list
@app.route("/unliked-article")
def unliked_article():
    global all_articles,not_liked_articles
    not_liked_articles.append(assign_val())
    return jsonify({"data":not_liked_articles,"status":"Success"})

# run the application
if __name__ == "__main__":
    app.run()