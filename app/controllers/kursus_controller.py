from flask import render_template, redirect, request
from app import db
from app.models import Kursus


def kursus_index():
    all_data = Kursus.query.all()
    return render_template('main.html', kursus = all_data)

def kursus_store():
    if request.method == 'POST':
        name = request.form['nama']

        my_data = Kursus(name)
        Kursus.addKursusBaru(my_data)

        return redirect('/')

def kursus_update():
    if request.method == 'POST':
        my_data = Kursus.query.get(request.form.get('id'))
        my_data.name = request.form['name']
        db.session.commit()
        return redirect('/')
    return "updating"

def kursus_delete(id):
    my_data = Kursus.query.get(id)
    Kursus.deleteKursus(my_data)

    return redirect('/')