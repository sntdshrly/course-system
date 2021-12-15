from flask import render_template, redirect, request
from app import db
from app.models import Administrator

def admin_index():
    all_data = Administrator.query.all()
    return render_template('admin.html', admin = all_data)

def admin_create():
    return render_template('tambah_admin.html')

def admin_store():
    if request.method == 'POST':
        name = request.form['nama']

        my_data = Administrator(name)
        db.session.add(my_data)
        db.session.commit()

        return redirect('/admin')

def admin_update(id=0):
    if request.method == 'POST':
        my_data = Administrator.query.get(request.form['id'])
        name = request.form['nama']
        my_data.editAdministrator(name)
        return redirect('/admin')
    else:
        data = Administrator.query.get(id)
        return render_template('edit_admin.html', admin=data)

def admin_delete(id):
    my_data = Administrator.query.get(id)
    Administrator.deleteAdministrator(my_data)
    return redirect('/admin')