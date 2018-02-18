from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, MetaData
# MetaData = MetaData()
# Author = Table('Authors',metadata, autoload=True, autoload_with=engine)
#
# stmt= select([Authors])
#
# result = connection.execute(stmt).fetchall()
#
# print(stmt)

################
#### Database ####
################




# engine = create_engine('sqlite:///census_nyc.sqlite')
#
# cennecting = engine.connect()
#
# stmt = 'select * from people'
#
# result_proxy = connection.execute(stmt)
#
# results = result_proxy.fetchall()

################
#### config ####
################

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rajat@localhost/postgres'
# app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)
# engine = create_engine("postgresql://postgres:rajat@localhost/postgres", pool_size=10, max_overflow=20)
# engine.connect()

class Books(db.Model):
     # __tablename__ = 'books'
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    authors = db.relationship('Authors', backref='owner', lazy='dynamic')
#     def __init__(self,condaname)
#     self.name=name
# if __name__ == "__main__":
#     db.create_all()
class Authors(db.Model):
    # __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    owner_id = db.Column(db.Integer, db.ForeignKey('books.id'))

# class DatabaseConnection:
    def __init__(self,name):
        self.name = name

@app.route('/list_all_users)')
def listallusers():
    mybooks = Books.query.all()
    return render_template('list_all_users.html',mybooks=Books)

if __name__ == '__main__':
    app.run()

# for i in Books:
#     print(i)
#     print("Nothing is Showing")

        # try:
        #     self.connection = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='rajat' port='5432'")
        #     self.connection.autocommit.Cursor()
        # except:
        #     print("cannot connect to database ")

#     def query_all(self):
#         self.Cursor.execute("select * from Authors INNER JOIN Books ON Books.id = Authors.id where Books.name = 'Galvin'")
#         bk = self.Cursor.fetchall()
#         for i in bk:
#             print("each Author : {0}".format(i))

#     database_connection = DatabaseConnection()
#     database_connection.query_all()
def Show(query):
    c. execute("select * from Authors INNER JOIN Books ON Books.id = Authors.id where Books.name = 'Galvin'")
    return c.fetchall()
    for i in Authors:
        print(c)
    return query.filter_by(name)
#
# wendy = my_filter(session.query(Authors)).one()
# print(wendy)
###################
### blueprints ####
###################

# from Redcarpet_Model.Book.views import Book_blueprint
# from Redcarpet_Model.Author.views import Author_blueprint
#
# # register the blueprints
# app.register_blueprint(Book_blueprint)
# app.register_blueprint(Author_blueprint)
