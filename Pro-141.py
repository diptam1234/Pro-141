from flask import Flask,jsonify,request
import csv

all_articles = []

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
disliked_articles = []

app = Flask(__name__)

@app.route('/get-articles')
def get_articles():
    return jsonify({
        "data" : all_articles[0],
        "status" : "success"
    })


@app.route('/liked-articles')   
def liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_article.append(article)
    return jsonify({
        "status" : "success"
    })


@app.route('/disliked-article')
def disliked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    disliked_article.append(article)
    return jsonify({
        "status" : "success"
    })
       
if __name__ == "__main__":
    app.run()













