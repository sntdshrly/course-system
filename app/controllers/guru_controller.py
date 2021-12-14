from flask import render_template, redirect, request
from app import db
from app.models import Guru

def guru_index():
    all_data = Guru.query.all()
    return render_template('guru.html', guru = all_data)

def guru_create():
    return render_template('tambah_guru.html')

def guru_store():
    if request.method == 'POST':
        name = request.form['nama']
        email = request.form['email']

        my_data = Guru(name, email)
        Guru.addGuruBaru(my_data)

        return redirect('/guru')

def guru_update(id=0):
    if request.method == 'POST':
        my_data = Guru.query.get(request.form['id'])
        name = request.form['nama']
        email = request.form['email']
        my_data.editGuru(name, email)
        return redirect('/guru')
    else:
        data = Guru.query.get(id)
        return render_template('edit_guru.html', guru=data)

def guru_delete(id):
    my_data = Guru.query.get(id)
    Guru.deleteGuru(my_data)
    return redirect('/guru')