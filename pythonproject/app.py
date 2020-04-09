from flask import Flask, render_template
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
    name = db.Column('name',db.String(),nullable=False)
    address = db.Column('address',db.String(),nullable=False)
    text = db.Column('text',db.String(),nullable=False)
    
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
    
    value = db.session.query(User).all()
    #user= q.all()
    
    
    
    return render_template("user.html", value=value)
    #return "User '{} has address {} and user got text :-{}' is from database".format(user.name, user.address, user.text)