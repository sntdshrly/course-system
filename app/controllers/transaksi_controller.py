from flask import render_template, redirect, request
from app import db
from app.models import Transaksi, Kursus, Siswa


def transaksi_index():
    all_data = Transaksi.query.all()
    return render_template('transaksi.html', transaksi = all_data)

def transaksi_create():
    all_kursus = Kursus.query.all()
    all_siswa = Siswa.query.all()
    return render_template('tambah_transaksi.html', kursus=all_kursus, siswa=all_siswa)

def transaksi_store():
    if request.method == 'POST':
        kursus = Kursus.query.get(request.form['kursus'])
        siswa = Siswa.query.get(request.form['siswa'])
        amount = request.form['amount']

        my_data = Transaksi(kursus, siswa, amount)
        Transaksi.tambahTransaksi(my_data)

        return redirect('/transaksi')

def transaksi_update(id=0):
    if request.method == 'POST':
        my_data = Transaksi.query.get(request.form['id'])
        amount = request.form['amount']
        # succeed = request.form['succeed']
        my_data.transact()
        return redirect('/transaksi')
    else:
        data = Transaksi.query.get(id)
        return render_template('edit_transaksi.html', transaksi=data)

def transaksi_delete(id):
    my_data = Transaksi.query.get(id)
    Transaksi.deleteTransaksi(my_data)
    return redirect('/transaksi')