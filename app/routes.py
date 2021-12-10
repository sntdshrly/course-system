from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Kursus

@app.route('/')
def Index():
    all_data = Kursus.query.all()
    print(all_data)
    return "all_data"


# this route is for inserting data to mysql database via html forms
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']

        my_data = Kursus(name)
        Kursus.addKursusBaru(my_data)

        return my_data


# this is our update route where we are going to update our employee
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Kursus.query.get(request.form.get('id'))

        my_data.name = request.form['name']

        db.session.commit()
        return redirect(url_for('Index'))


# This route is for deleting our employee
@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = Kursus.query.get(id)
    db.session.delete(my_data)
    db.session.commit()

    return redirect(url_for('Index'))