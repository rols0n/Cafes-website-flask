import os
import pandas as pd
from flask import Flask, redirect, url_for, render_template, request
from flask_bootstrap import Bootstrap
from wtforms import SubmitField, StringField, PasswordField, validators
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from forms import AddPOST
app = Flask(__name__)
app.config['SECRET_KEY'] = 'jd'
Bootstrap(app)

db_name  = 'cafes.db'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Cafe(db.Model):
    __tablename__ = 'cafe'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    map_url = db.Column(db.String())
    img_url = db.Column(db.String())
    location = db.Column(db.String())
    has_sockets = db.Column(db.String())
    has_toilet = db.Column(db.String())
    has_wifi = db.Column(db.String())
    can_take_calls = db.Column(db.String())
    seats = db.Column(db.String())
    coffee_price = db.Column(db.String())

db.create_all()


@app.route('/', methods=['GET', 'POST'])
def home():
    # Getting id's
    id = 0
    id_list = []
    testing = True

    while testing:
        for id in range(1, 200):
            cafe = Cafe.query.filter_by(id=id).first()
            if cafe != None:
                id_list += [id]
            else:
                testing = False
    id_lists = len(id_list)
    return render_template('index.html', id=id, id_list=id_list, Cafe=Cafe, id_lists=id_lists)


@app.route('/new_post', methods=['POST', 'GET'])
def new_post():
    form = AddPOST()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=request.form.get('name'),
            map_url=request.form.get('map_url'),
            img_url=request.form.get('img_url'),
            location=request.form.get('location'),
            has_sockets=request.form.get('has_sockets'),
            has_toilet=request.form.get('has_toilet'),
            has_wifi=request.form.get('has_wifi'),
            can_take_calls = request.form.get('can_take_calls'),
            seats=request.form.get('seats'),
            coffee_price=request.form.get('coffee_price'),
        )
        db.session.add(new_cafe)
        db.session.commit()
        # id_of_last_object = Cafe.query.filter_by(map_url=request.form.get('map_url').last())
        # global data
        # data = id_of_last_object.id
        return redirect(url_for("home"))

    return render_template('post.html', form=form)
if __name__ == "__main__":
    app.run(debug=True)

