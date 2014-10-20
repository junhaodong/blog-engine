import sqlite3

conn = sqlite3.connect("p.db")

q = "create table posts(title text, post text)"
c = conn.cursor()
c.execute(q)

q="""
create table comments(post_title text, comment text)
"""
c.execute(q);
conn.commit();
