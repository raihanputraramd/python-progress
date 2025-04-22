class Kendaraan():
    def bergerak(self):
        print("Kendaraan Bergerak")


class Motor(Kendaraan):
    def bergerak(self):
        print("Motor bergerak roda 2")


class Mobil(Kendaraan):
    def bergerak(self):
        print("Mobil bergerak roda 4")


def jalankan_kendaraan(kendaraan):
    kendaraan.bergerak()

jalankan_kendaraan(Motor())
jalankan_kendaraan(Mobil())


# Soal: Koleksi Objek & Polymorphism
# Buatlah:
# Sebuah class induk bernama Hewan yang memiliki method suara().
# Buat 3 class turunan: Kucing, Anjing, dan Ayam, masing-masing override method suara() dengan suara khas hewan tersebut.
# Buat sebuah list berisi objek dari berbagai class turunan tadi.
# Buat perulangan untuk memanggil suara() dari setiap objek di dalam list tersebut.

class Hewan():
    def suara(self):
        print('Hewan Bersuara')


class Kucing(Hewan):
    def suara(self):
        print("Meong!!")


class Anjing(Hewan):
    def suara(self):
        print("Woof")


class Ayam(Hewan):
    def suara(self):
        print("Kukuruyuk")


hewan_list = [Kucing(), Anjing(), Ayam()]

for hewan in hewan_list:
    hewan.suara()