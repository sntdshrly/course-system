from abc import ABC, abstractmethod

class Siswa(ABC):
    @abstractmethod
    def viewInfoSiswa(self):
        pass
    def addSiswaBaru(self):
        pass

class SiswaLama(Siswa):
    idSiswa = ""
    namaSiswa = ""
    alamatSiswa = ""
    emailSiswa = ""
    def viewInfoSiswa(self):
        pass
    def addSiswaBaru(self):
        pass

class SiswaBaru(Siswa):
    idSiswa = ""
    namaSiswa = ""
    alamatSiswa = ""
    emailSiswa = ""
    def viewInfoSiswa(self):
        pass
    def addSiswaBaru(self):
        pass

class Guru():
    idGuru = ""
    namaGuru = ""
    emailGuru = ""
    def getGuru(self):
        pass
    def viewInfoSiswa(self):
        pass
    def addGuruBaru(self):
        pass

class Administrator():
    idAdmin = ""
    namaAdmin = ""
    def viewKursus(self):
        pass
    def manageKursus(self):
        pass

class Kursus():
    idKursus = ""
    namaKursus = ""
    def addKursusBaru(self):
        pass
    def deleteKursus(self):
        pass
    def getListKursus(self):
        pass

class RegistrasiKursus():
    idKursus = ""
    namaKursus = ""
    dateRegistration = ""
    def registrateKursus(self):
        pass
    def viewInfoKursus(self):
        pass

class Jadwal():
    idJadwal = ""
    idKursus = ""
    idSiswa = ""
    idGuru = ""
    date = ""
    def setJadwal(self):
        pass
    def getJadwal(self):
        pass

class Transaksi:
    idTransaksi = ""
    idKursus = ""
    idSiswa = ""
    amount = 0
    succeed = bool
    def transact(self):
        pass
    def getSucceed(self):
        pass