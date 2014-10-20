import sqlite3
import csv

conn = sqlite3.connect('p.db')

c=conn.cursor()
BASE="INSERT INTO posts VALUES('%(tltle)s',%(post)s)"
for line in csv.DictReader(open("posts.csv")):
    q = BASE%line
    print q
    c.execute(q)

BASE="INSERT INTO comments VALUES('%(post_title)s',%(comment)s)"
for line in csv.DictReader(open("comments.csv")):
    q = BASE%line
    print q
    c.execute(q)

conn.commit()
