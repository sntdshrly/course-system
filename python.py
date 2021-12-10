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
    def viewInfoSiswa():
        pass
    def addGuruBaru():
        pass

class Administrator():
    idAdmin = ""
    namaAdmin = ""
    def viewKursus():
        pass
    def manageKursus():
        pass

class Kursus():
    idKursus = ""
    namaKursus = ""
    def addKursusBaru():
        pass
    def deleteKursus():
        pass
    def getListKursus():
        pass

class RegistrasiKursus():
    idKursus = ""
    namaKursus = ""
    dateRegistration = ""
    def registrateKursus():
        pass
    def viewInfoKursus():
        pass

class Jadwal():
    idJadwal = ""
    idKursus = ""
    idSiswa = ""
    idGuru = ""
    date = ""
    def setJadwal():
        pass
    def getJadwal():
        pass

class Transaksi:
    idTransaksi = ""
    idKursus = ""
    idSiswa = ""
    amount = 0
    succeed = bool
    def transact():
        pass
    def getSucceed():
        pass