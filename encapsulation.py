class AkunBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.__saldo = saldo


    def lihat_saldo(self):
        return f"Saldo: Rp {self.__saldo}"
    
    
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setor berhasil. Saldo sekarang: Rp {self.__saldo}")
        else:
            print("Jumlah Tidak Valid")
    
    
    def tarik(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Tarik berhasil, Sisa Saldo: Rp {self.__saldo}")
        else:
            print("Saldo tidak cukup")


# akun = AkunBank("Raihan", 1000000)
# print(akun.lihat_saldo())
# akun.setor(500000)
# akun.tarik(200000)


# 🔒 Latihan Soal 1: Rekening Bank
# Buatlah class RekeningBank dengan:
# Atribut private __pemilik dan __saldo
# Method:
# __init__(self, pemilik, saldo_awal) → untuk set pemilik dan saldo
# cek_saldo() → menampilkan saldo saat ini
# setor(jumlah) → menambah saldo (hanya jika jumlah positif)
# tarik(jumlah) → mengurangi saldo (hanya jika saldo cukup)
# ganti_nama(nama_baru) → mengubah nama pemilik rekening

class RekeningBank:
    def __init__(self, pemilik, saldo_awal):
        self.__pemilik = pemilik
        self.__saldo_awal = saldo_awal
    

    def cek_saldo(self):
        print(f"Saldo Saat ini: Rp {self.__saldo_awal}")
    

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo_awal += jumlah
            print(f"Jumlah Saldo Saat ini: Rp {self.__saldo_awal}")
        else:
            print("Jumlah Tidak Valid")
    

    def tarik(self, jumlah):
        if jumlah <= self.__saldo_awal <= 100:
            self.__saldo_awal -= jumlah
            print(f"Jumlah Saldo Saat ini: Rp {self.__saldo_awal}")
        else:
            print("Saldo tidak mencukupi")
    

    def ganti_nama(self, nama_baru):
        self.__pemilik = nama_baru
        print(f"Pemilik baru saat ini: {self.__pemilik}")

rek = RekeningBank("Raihan", 1000000)
rek.setor(200000)
rek.tarik(300000)
rek.ganti_nama("Raihan P.")
rek.cek_saldo()


# 🔐 Latihan Soal 2: Data Mahasiswa
# Buat class Mahasiswa yang memiliki:
# Atribut private: __nama, __nilai
# Method:
# __init__(self, nama, nilai_awal)
# lihat_nilai() → menampilkan nilai
# ubah_nilai(nilai_baru) → hanya bisa ubah nilai jika nilai_baru antara 0-100

# 🛑 Catatan:
# Jangan akses atribut __nama atau __saldo langsung dari luar class.
# Gunakan method (fungsi) sebagai interface antar class dan pengguna.

class Mahasiswa:
    def __init__(self, nama, nilai):
        self.__nama = nama
        self.__nilai = nilai
    

    def lihat_nilai(self):
        print(f"Nilai matematika Saat ini: {self.__nilai}")

    
    def ubah_nilai(self, nilai_baru):
        if 0 <= nilai_baru:
            self.__nilai = nilai_baru
            print(f"Nilai matematika Saat ini: {self.__nilai}")
        else:
            print("Nilai tidak valid")
    

mhs = Mahasiswa("Raihan", 50)
mhs.lihat_nilai()
mhs.ubah_nilai(70)

