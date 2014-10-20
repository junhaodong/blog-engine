import sqlite3, csv

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

#def populate():
#    BASE="INSERT INTO posts VALUES('%(title)s',%(post)s)"
#    for line in csv.DictReader(open("posts.csv")):
#        q = BASE%line
#        print q
#        c.execute(q)
#    BASE="INSERT INTO comments VALUES('%(post_title)s',%(comment)s)"
#    for line in csv.DictReader(open("comments.csv")):
#        q = BASE%line
#        print q
#        c.execute(q)
#    conn.commit()

# May consider using *args to take a variable amount of arguments
# if we add more columns/values
def insert(table, post_title, text):
    #if table == "posts":
    #    textType = post
    #else:
    #    textType = comment
    conn = sqlite3.connect("p.db")
    c = conn.cursor()
    q = "INSERT INTO {0} VALUES('{1}','{2}')"
    q = q.format(table, post_title, text)
    c.execute(q)
    conn.commit()
    conn.close()

# Returns a list of titles
def getTitles():
    conn = sqlite3.connect("p.db")
    c = conn.cursor()
    q = "SELECT post_title FROM posts"
    results = c.execute(q)
    titles = [r[0] for r in results]
    conn.close()
    return titles