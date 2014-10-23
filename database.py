import sqlite3

# Assume no duplicate post_titles
def create():
    conn = sqlite3.connect("p.db")
    c = conn.cursor()
    q = "CREATE TABLE IF NOT EXISTS posts(post_title text, post text)"
    c.execute(q)
    q = "CREATE TABLE IF NOT EXISTS comments(post_title text, comment text)"
    c.execute(q)
    conn.commit()
    conn.close()

# May consider using *args to take a variable amount of arguments
# if we add more columns/values
def insert(table, post_title, text):
    conn = sqlite3.connect("p.db")
    c = conn.cursor()
    q = "INSERT INTO {0} VALUES('{1}','{2}')"
    q = q.format(table, post_title, text)
    c.execute(q)
    conn.commit()
    conn.close()

# Note: all `get` functions return lists

def getTitles():
    conn = sqlite3.connect("p.db")
    c = conn.cursor()
    q = "SELECT post_title FROM posts"
    results = c.execute(q)
    titles = [r[0] for r in results]
    conn.commit()
    conn.close()
    return titles

def getPost(post_title):
    conn = sqlite3.connect("p.db")
    c = conn.cursor()
    q = "SELECT post FROM posts WHERE post_title=='{0}'"
    q = q.format(post_title)
    results = c.execute(q)
    post = [r[0] for r in results]
    conn.commit()
    conn.close()
    return post

def getComments(post_title):
    conn = sqlite3.connect("p.db")
    c = conn.cursor()
    q = "SELECT comment FROM comments WHERE post_title=='{0}'"
    q = q.format(post_title)
    results = c.execute(q)
    comments = [r[0] for r in results]
    conn.commit()
    conn.close()
    return comments
