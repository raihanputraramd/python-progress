# Buatlah kelas abstrak bernama AlatMusik:
# Memiliki method abstrak bunyi()
# Buat 3 class turunan dari AlatMusik:
# Gitar, Piano, dan Drum
# Masing-masing mengimplementasikan method bunyi() sesuai dengan suara alat musik tersebut.
# Buat class PemainMusik:
# Memiliki atribut alat, yang merupakan objek dari class turunan AlatMusik
# Method mainkan_musik() akan memanggil bunyi() dari alat musik tersebut
# Buat beberapa objek PemainMusik yang menggunakan alat musik berbeda, dan jalankan mainkan_musik() mereka.

from abc import ABC, abstractmethod

class AlatMusik(ABC):
    @abstractmethod
    def bunyi(self):
        pass


class Gitar(AlatMusik):
    def bunyi(self):
        print("Jreng")


class Piano(AlatMusik):
    def bunyi(self):
        print("do re mi")


class Drum(AlatMusik):
    def bunyi(self):
        print("Dug stak")


class PemainMusik:
    def __init__(self, alat):
        self.alat = alat
    

    def mainkan_musik(self):
        self.alat.bunyi()

raihan = PemainMusik(Gitar())
raihan.mainkan_musik()