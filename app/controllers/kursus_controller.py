from flask import render_template, redirect, request
from app import db
from app.models import Kursus


def kursus_index():
    all_data = Kursus.query.all()
    return render_template('kursus.html', kursus = all_data)

def kursus_create():
    return render_template('tambah_kursus.html')

def kursus_store():
    if request.method == 'POST':
        name = request.form['nama']

        my_data = Kursus(name)
        Kursus.addKursusBaru(my_data)

        return redirect('/kursus')

def kursus_update(id=0):
    if request.method == 'POST':
        my_data = Kursus.query.get(request.form['id'])
        my_data.editKursus(request.form['nama'])
        return redirect('/kursus')
    else:
        data = Kursus.query.get(id)
        return render_template('tambah_kursus.html', kursus=data)

def kursus_delete(id):
    my_data = Kursus.query.get(id)
    Kursus.deleteKursus(my_data)

    return redirect('/kursus')