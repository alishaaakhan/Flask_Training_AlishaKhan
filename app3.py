from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Database Configuration code
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flaskproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print("Alisha")
db = SQLAlchemy(app)


#Database model
class Employee(db.Model):
    eid = db.Column(db.Integer, primary_key = True)
    ename = db.Column(db.String(80), nullable = True)
    email = db.Column(db.String(20), nullable = True)
    phone_num = db.Column(db.String(12), nullable = True)
    ecompany = db.Column(db.String(80), nullable = True)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug = True)