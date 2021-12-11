from flask import render_template, redirect, request
from app import db
from app.models import Guru

def guru_index():
    all_data = Guru.query.all()
    return render_template('main.html', guru = all_data)

def guru_store():
    if request.method == 'POST':
        name = request.form['nama']
        email = request.form['email']
        alamat = request.form['alamat']

        my_data = Guru(name, email)
        Guru.addGuruBaru(my_data)

        return redirect('/')

def guru_update():
    if request.method == 'POST':
        my_data = Guru.query.get(request.form.get('id'))
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        db.session.commit()
        return redirect('/')
    return "updating"

def guru_delete(id):
    my_data = Guru.query.get(id)
    return redirect('/')