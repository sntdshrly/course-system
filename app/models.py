from app import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy(app)

class Kursus(db.Model):
    __tablename__ = "kursus"

    idKursus = db.Column(db.Integer, primary_key=True, autoincrement=True)
    namaKursus = db.Column(db.String(255), nullable=False)

    def addKursusBaru(self):
        db.session.add(self)
        db.session.commit()

    def editKursus(self, nama):
        self.namaKursus = nama
        db.session.commit()

    def deleteKursus(self):
        db.session.delete(self)
        db.session.commit()

    def getListKursus(self):
        self.query.all()

    def __init__(self, namaKursus):
        self.namaKursus = namaKursus

    def __repr__(self):
        return f"{self.namaKursus}"

class Siswa(db.Model):
    __tablename__ = "siswa"

    idSiswa = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    namaSiswa = db.Column(db.String(255), nullable=False)
    alamatSiswa = db.Column(db.String(255), nullable=False)
    emailSiswa = db.Column(db.String(255), nullable=False)

    def __init__(self, nama, alamat, email):
        self.namaSiswa = nama
        self.alamatSiswa = alamat
        self.emailSiswa = email

    def viewInfoSiswa(self):
        return f"Nama : {self.namaSiswa}\nAlamat : {self.alamatSiswa}\nEmail : {self.emailSiswa}"

    def addSiswaBaru(self):
        db.session.add(self)
        db.session.commit()

    def editSiswa(self, nama, alamat, email):
        self.namaSiswa = nama
        self.emailSiswa = email
        self.alamatSiswa = alamat
        db.session.commit()

    def deleteSiswa(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"{self.namaSiswa}"

class Guru(db.Model):
    __tablename__ = "guru"

    idGuru = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    namaGuru = db.Column(db.String(255), nullable=False)
    emailGuru = db.Column(db.String(255), nullable=False)

    def __init__(self, nama, email):
        self.namaGuru = nama
        self.emailGuru = email

    def getGuru(self):
        return f"Nama : {self.namaGuru}\nEmail : {self.emailGuru}"

    def viewInfoSiswa(self, siswa):
        return self.query.filter_by('jadwal.idSiswa'==siswa.idSiswa).get()

    def addGuruBaru(self):
        db.session.add(self)
        db.session.commit()

    def editGuru(self, nama, email):
        self.namaGuru = nama
        self.emailGuru = email
        db.session.commit()

    def deleteGuru(self):
        db.session.delete(self)
        db.session.commit()

class Administrator(db.Model):
    __tablename__ = "admin"

    idAdmin = db.Column(db.Integer, primary_key=True, autoincrement=True)
    namaAdmin = db.Column(db.String(255), nullable=False)

    def __init__(self, name):
        self.namaAdmin = name

    def viewKursus(self):
        return Kursus.query.all()

    def editAdministrator(self, nama):
        self.namaAdmin = nama
        db.session.commit()

    def deleteAdministrator(self):
        db.session.delete(self)
        db.session.commit()



    def manageKursus(self, kursus: Kursus):
        return kursus

class RegistrasiKursus(db.Model):
    __tablename__ = "registrasi"

    idKursus = db.Column(db.Integer, primary_key=True, autoincrement=True)
    namaKursus = db.Column(db.String(255), nullable=False)
    dateRegistration = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, id, nama, date=0):
        self.idKursus = id
        self.namaKursus= nama
        self.dateRegistration = date

    def registrateKursus(self, kursus: Kursus):
        db.session.add(kursus)
        db.session.commit()

    def viewInfoKursus(self, id):
        return Kursus.query.get(id)

class Jadwal(db.Model):
    __tablename__ = "jadwal"

    idJadwal = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idKursus = db.Column(db.Integer, db.ForeignKey('kursus.idKursus'), nullable=False)
    kursus = db.relationship('Kursus', backref=db.backref('jadwal', lazy=True))
    idSiswa = db.Column(db.Integer, db.ForeignKey('siswa.idSiswa'), nullable=False)
    siswa = db.relationship('Siswa', backref=db.backref('jadwal', lazy=True))
    idGuru = db.Column(db.Integer, db.ForeignKey('guru.idGuru'), nullable=False)
    guru = db.relationship('Guru', backref=db.backref('jadwal', lazy=True))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, kursus, siswa, guru):
        self.kursus = kursus
        self.siswa = siswa
        self.guru = guru

    def setJadwal(self):
        db.session.add(self)
        db.session.commit()

    def editJadwal(self, kursus, guru, siswa):
        self.kursus = kursus
        self.guru = guru
        self.siswa = siswa
        db.session.commit()

    def deleteJadwal(self):
        db.session.delete(self)
        db.session.commit()

    def getJadwal(self):
        return self

class Transaksi(db.Model):
    __tablename__ = "transaksi"

    idTransaksi = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idKursus = db.Column(db.Integer, db.ForeignKey('kursus.idKursus'), nullable=False)
    kursus = db.relationship('Kursus', backref=db.backref('transaksi', lazy=True))
    idSiswa = db.Column(db.Integer, db.ForeignKey('siswa.idSiswa'), nullable=False)
    siswa = db.relationship('Siswa', backref=db.backref('transaksi', lazy=True))
    amount = db.Column(db.Integer, nullable=False)
    succeed = db.Column(db.Boolean, default=True)

    def tambahTransaksi(self):
        db.session.add(self)
        db.session.commit()

    def deleteTransaksi(self):
        db.session.delete(self)
        db.session.commit()

    def __init__(self, kursus, siswa, amount):
        self.kursus = kursus
        self.siswa = siswa
        self.amount = amount

    def transact(self):
        self.succeed = not self.succeed
        db.session.commit()

    def getSucceed(self):
        return self.succeed