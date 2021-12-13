from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Kursus

from app.controllers.kursus_controller import *

@app.route('/')
def index():
    return render_template('main.html')

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
    return kursus_update(id)\

@app.route('/kursus/update', methods=['POST'])
def edit_kursus():
    return kursus_update()


@app.route('/kursus/delete/<int:id>/')
def delete_kursus(id):
    return kursus_delete(id)