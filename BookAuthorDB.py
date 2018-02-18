import sqlite3
from Authors import Authors
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, MetaData

conn = sqlite3.connect('Author.db')

c= conn.cursor()

emp1 = Authors

c. execute("select * from Authors INNER JOIN Books ON Books.id = Authors.id where Books.name = 'Galvin'")

print(c.fetchall())

conn.commit()
conn.close()
