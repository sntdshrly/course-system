from flask import render_template, redirect, request
from app import db
from app.models import Siswa

def siswa_index():
    all_data = Siswa.query.all()
    return render_template('main.html', siswa = all_data)

def siswa_store():
    if request.method == 'POST':
        name = request.form['nama']
        email = request.form['email']
        alamat = request.form['alamat']

        my_data = Siswa(name, email, alamat)
        Siswa.addSiswaBaru(my_data)

        return redirect('/')

def siswa_update():
    if request.method == 'POST':
        my_data = Siswa.query.get(request.form.get('id'))
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.alamat = request.form['alamat']
        db.session.commit()
        return redirect('/')
    return "updating"

def siswa_delete(id):
    my_data = Siswa.query.get(id)
    return redirect('/')