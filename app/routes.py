from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Kursus

from app.controllers.kursus_controller import *
from app.controllers.siswa_controller import *
from app.controllers.guru_controller import *

@app.route('/')
def index():
    return render_template('main.html')




# KURSUS
@app.route('/kursus')
def index_kursus():
    return kursus_index()

@app.route('/kursus/create')
def create_kursus():
    return kursus_create()

@app.route('/kursus/insert', methods=['POST'])
def insert_kursus():
    return kursus_store()

@app.route('/kursus/update/<int:id>', methods=['GET', 'POST'])
def update_kursus(id):
    return kursus_update(id)

@app.route('/kursus/update', methods=['POST'])
def edit_kursus():
    return kursus_update()


@app.route('/kursus/delete/<int:id>/')
def delete_kursus(id):
    return kursus_delete(id)





# SISWA
@app.route('/siswa')
def index_siswa():
    return siswa_index()

@app.route('/siswa/create')
def create_siswa():
    return siswa_create()

@app.route('/siswa/insert', methods=['POST'])
def insert_siswa():
    return siswa_store()

@app.route('/siswa/update/<int:id>', methods=['GET', 'POST'])
def update_siswa(id):
    return siswa_update(id)

@app.route('/siswa/update', methods=['POST'])
def edit_siswa():
    return siswa_update()


@app.route('/siswa/delete/<int:id>/')
def delete_siswa(id):
    return siswa_delete(id)





# GURU
@app.route('/guru')
def index_guru():
    return guru_index()

@app.route('/guru/create')
def create_guru():
    return guru_create()

@app.route('/guru/insert', methods=['POST'])
def insert_guru():
    return guru_store()

@app.route('/guru/update/<int:id>', methods=['GET', 'POST'])
def update_guru(id):
    return guru_update(id)

@app.route('/guru/update', methods=['POST'])
def edit_guru():
    return guru_update()


@app.route('/guru/delete/<int:id>/')
def delete_guru(id):
    return guru_delete(id)