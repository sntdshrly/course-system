from flask import render_template, redirect, request
from app import db
from app.models import Siswa

def siswa_index():
    all_data = Siswa.query.all()
    return render_template('siswa.html', siswa = all_data)

def siswa_create():
    return render_template('tambah_siswa.html')

def siswa_store():
    if request.method == 'POST':
        name = request.form['nama']
        email = request.form['email']
        alamat = request.form['alamat']

        my_data = Siswa(name, alamat, email)
        Siswa.addSiswaBaru(my_data)

        return redirect('/siswa')

def siswa_update(id=0):
    if request.method == 'POST':
        my_data = Siswa.query.get(request.form['id'])
        print(my_data)
        nama = request.form['nama']
        email = request.form['email']
        alamat = request.form['alamat']
        my_data.editSiswa(nama, alamat, email)
        return redirect('/siswa')
    else:
        data = Siswa.query.get(id)
        return render_template('edit_siswa.html', siswa=data)

def siswa_delete(id):
    my_data = Siswa.query.get(id)
    Siswa.deleteSiswa(my_data)
    return redirect('/siswa')