# Buat class Hewan sebagai class abstrak.
# Di dalam Hewan, buat method abstrak suara().
# Buat class turunan: Kucing, Anjing, dan Ayam.
# Masing-masing class isi method suara() dengan suara hewan masing-masing.
# Buat list berisi objek dari ketiga class turunan tadi.
# Gunakan perulangan untuk memanggil method suara() satu per satu.

from abc import ABC, abstractmethod

class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass

class Kucing(Hewan):
    def suara(self):
        print("Meong")


class Anjing(Hewan):
    def suara(self):
        print("Woof")


class Ayam(Hewan):
    def suara(self):
        print('Kukuruyuk')

hewan_list = [Kucing(), Anjing(), Ayam()]

for list in hewan_list:
    list.suara()