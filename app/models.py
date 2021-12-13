from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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