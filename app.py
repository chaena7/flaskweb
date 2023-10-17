from flask import Flask, render_template, jsonify, request
from utils import get_movie_info

app = Flask(__name__)

# Mongo DB 사용 준비
from pymongo import MongoClient
client = MongoClient('127.0.0.1')
db = client.db1

@app.route("/")
def home():
    # templates 디렉토리의 파일을 출력
    return render_template("index.html")


@app.route('/memo', methods=['GET'])
def listing():
    articles = list(db.articles.find({}, {'_id':False}))
    return jsonify({'all_articles':articles})

@app.route('/memo', methods=['POST'])
def saving():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    title, image, description = get_movie_info(url_receive)
    doc = {
        'title':title,
        'image':image,
        'description':description,
        'url':url_receive,
        'comment':comment_receive
    }
    db.articles.insert_one(doc)

    return jsonify({'msg':'저장이 완료되었습니다.'})

if __name__=='__main__':
    app.run('0.0.0.0', port=5000, debug=True)

