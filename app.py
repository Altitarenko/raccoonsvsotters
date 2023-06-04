import sqlite3
import os
import random
from flask import Flask, render_template
from werkzeug.exceptions import abort



app = Flask(__name__)

images = [
    "https://raccoonsvsotters.s3.eu-north-1.amazonaws.com/1.jpeg",
    "https://raccoonsvsotters.s3.eu-north-1.amazonaws.com/2.jpeg",
    "https://raccoonsvsotters.s3.eu-north-1.amazonaws.com/3.jpeg",  
    "https://raccoonsvsotters.s3.eu-north-1.amazonaws.com/4.jpeg",
    "https://raccoonsvsotters.s3.eu-north-1.amazonaws.com/5.jpeg",
    "https://raccoonsvsotters.s3.eu-north-1.amazonaws.com/6.jpeg",
    "https://raccoonsvsotters.s3.eu-north-1.amazonaws.com/7.jpeg",
    "https://raccoonsvsotters.s3.eu-north-1.amazonaws.com/8.jpeg",
    "https://raccoonsvsotters.s3.eu-north-1.amazonaws.com/9.jpeg",
    "https://raccoonsvsotters.s3.eu-north-1.amazonaws.com/10.jpeg",
    "https://raccoonsvsotters.s3.eu-north-1.amazonaws.com/11.jpeg",
    "https://raccoonsvsotters.s3.eu-north-1.amazonaws.com/12.jpeg",
    "https://raccoonsvsotters.s3.eu-north-1.amazonaws.com/13.jpeg",
    "https://raccoonsvsotters.s3.eu-north-1.amazonaws.com/14.jpeg",
    "https://raccoonsvsotters.s3.eu-north-1.amazonaws.com/15.jpeg",
]



def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    url = random.choice(images)
    return render_template('post.html', post=post, url=url)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 80)))
