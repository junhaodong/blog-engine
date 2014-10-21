#!/usr/bin/python
from flask import Flask, render_template, request
import database

app = Flask(__name__)


@app.route("/")
def main():
    post_title = request.args.get("post_title",None)
    post_body = request.args.get("post_body",None)
    button = request.args.get("button",None)
    print button
    if button == None:
        titles = database.getTitles()
        return render_template("home.html", titles=titles)
    else:
        database.insert('posts',post_title,post_body)
        return post(post_title)

# SEE FLASK DOCUMENTATION regarding <post_title>
# Use 'get' or 'post'? pros and cons
@app.route("/<post_title>")  #methods=['GET','POST'])
def post(post_title):
    post = database.getPost(post_title)
    #print post
    #print 'LOOK AT MEEEEEEEEEEEEE'
    comments = database.getComments(post_title)
    return render_template("post.html", post_title=post_title, post=post, comments=comments )

if __name__ == "__main__":
    app.debug=True
    database.create()
    #app.run()
    app.run(host="0.0.0.0",port=5000)
