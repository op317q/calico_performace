from flask import Flask
import sqlalchemy
from faker import Faker

#import db, User

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)

db.init_app(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())
    text = db.Column(db.String())
    
    def __init__( self, name, address, text):
        self.name = name
        self.address = address
        self.text = text


@app.route('/test')
def test():
    return 'Hello World! I am from docker!'

@app.route('/')
@app.route('/test_db')
def test_db():
    db.create_all()
    db.session.commit()
    
    fake = Faker()
    name = fake.name()
    address = fake.address()
    text = fake.text()
    
    print("name := "+ name )
    print("address:= "+ address)
    print("text:= "+text)
    
    
    u = User(name, address, text)
    db.session.add(u)
    db.session.commit()
    
    q = db.session.query(User).from_statement(
    sqlalchemy.text("SELECT * FROM users where name=:n")).params(n = name)
    user= q.first()

    return "User '{} has address {} and user got text :-{}' is from database".format(user.name, user.address, user.text)