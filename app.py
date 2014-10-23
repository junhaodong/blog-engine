#!/usr/bin/python
from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

@app.route("/")
def main():
    post_title = request.args.get("post_title",None)
    post_body = request.args.get("post_body",None)
    post_button = request.args.get("post_button",None)

    if post_button == None:
        titles = database.getTitles()
        return render_template("home.html", titles=titles)
    else:
        database.insert('posts',post_title,post_body)
        return redirect(url_for('post',post_title=post_title))

@app.route("/<post_title>")
def post(post_title):
    posts = database.getPost(post_title)
    comment_button = request.args.get("comment_button",None)

    if comment_button == None:
        comments = database.getComments(post_title)
        return render_template("post.html",
                               post_title=post_title, 
                               posts=posts,comments=comments)
    else:
        newComment = request.args.get("comment",None)
        database.insert('comments',post_title,newComment)
        comments = database.getComments(post_title)
        return render_template("post.html",
                               post_title=post_title,
                               posts=posts,comments=comments)

if __name__ == "__main__":
    #app.debug=True
    database.create()
    app.run()
