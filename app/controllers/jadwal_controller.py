from flask import render_template, redirect, request
from app.models import Jadwal, Kursus, Guru, Siswa

def jadwal_index():
    all_data = Jadwal.query.all()
    return render_template('jadwal.html', jadwal = all_data)

def jadwal_create():
    all_kursus = Kursus.query.all()
    all_guru = Guru.query.all()
    all_siswa = Siswa.query.all()
    return render_template('tambah_jadwal.html', kursus=all_kursus, guru=all_guru, siswa=all_siswa)

def jadwal_store():
    if request.method == 'POST':
        guru = Guru.query.get(request.form['guru'])
        kursus = Kursus.query.get(request.form['kursus'])
        siswa = Siswa.query.get(request.form['siswa'])

        my_data = Jadwal(kursus, siswa, guru)
        my_data.setJadwal()

        return redirect('/jadwal')

def jadwal_update(id=0):
    if request.method == 'POST':
        my_data = Jadwal.query.get(request.form['id'])
        kursus = Kursus.query.get(request.form['kursus'])
        guru = Guru.query.get(request.form['guru'])
        siswa = Siswa.query.get(request.form['siswa'])

        my_data.editJadwal(kursus, guru, siswa)
        return redirect('/jadwal')
    else:
        all_jadwal = Jadwal.query.get(id)
        all_kursus = Kursus.query.all()
        all_guru = Guru.query.all()
        all_siswa = Siswa.query.all()
        return render_template('edit_jadwal.html', jadwal=all_jadwal, kursus=all_kursus, guru=all_guru, siswa=all_siswa)

def jadwal_delete(id):
    my_data = Jadwal.query.get(id)
    Jadwal.deleteJadwal(my_data)
    return redirect('/jadwal')