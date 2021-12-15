from app import app
from app.controllers.guru_controller import *
from app.controllers.kursus_controller import *
from app.controllers.siswa_controller import *
from app.controllers.admin_controller import *
from app.controllers.jadwal_controller import *
from app.controllers.transaksi_controller import *


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


# ADMIN
@app.route('/admin')
def index_admin():
    return admin_index()

@app.route('/admin/create')
def create_admin():
    return admin_create()

@app.route('/admin/insert', methods=['POST'])
def insert_admin():
    return admin_store()

@app.route('/admin/update/<int:id>', methods=['GET', 'POST'])
def update_admin(id):
    return admin_update(id)

@app.route('/admin/update', methods=['POST'])
def edit_admin():
    return admin_update()


@app.route('/admin/delete/<int:id>/')
def delete_admin(id):
    return admin_delete(id)


# JADWAL
@app.route('/jadwal')
def index_jadwal():
    return jadwal_index()

@app.route('/jadwal/create')
def create_jadwal():
    return jadwal_create()

@app.route('/jadwal/insert', methods=['POST'])
def insert_jadwal():
    return jadwal_store()

@app.route('/jadwal/update/<int:id>', methods=['GET', 'POST'])
def update_jadwal(id):
    return jadwal_update(id)

@app.route('/jadwal/update', methods=['POST'])
def edit_jadwal():
    return jadwal_update()


@app.route('/jadwal/delete/<int:id>/')
def delete_jadwal(id):
    return jadwal_delete(id)



# TRANSAKSI

@app.route('/transaksi')
def index_transaksi():
    return transaksi_index()

@app.route('/transaksi/create')
def create_transaksi():
    return transaksi_create()

@app.route('/transaksi/insert', methods=['POST'])
def insert_transaksi():
    return transaksi_store()

@app.route('/transaksi/update/<int:id>', methods=['GET', 'POST'])
def update_transaksi(id):
    return transaksi_update(id)

@app.route('/transaksi/update', methods=['POST'])
def edit_transaksi():
    return transaksi_update()


@app.route('/transaksi/delete/<int:id>/')
def delete_transaksi(id):
    return transaksi_delete(id)