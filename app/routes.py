from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Kursus

from app.controllers.kursus_controller import *

@app.route('/')
def index():
    return kursus_index()

@app.route('/insert', methods=['POST'])
def insert():
    return kursus_store()

@app.route('/update', methods=['GET', 'POST'])
def update():
    return kursus_update()


@app.route('/delete/<int:id>/')
def delete(id):
    return kursus_delete(id)