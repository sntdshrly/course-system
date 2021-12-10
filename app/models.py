from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# example
class Kursus(db.Model):
    __tablename__ = "kursus"

    idKursus = db.Column(db.Integer, primary_key=True)
    namaKursus = db.Column(db.String(255), nullable=False)

    def addKursusBaru(self):
        db.session.add(self)
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