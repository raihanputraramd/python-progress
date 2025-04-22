# Ada class Kendaraan: punya nama dan method jalan().
# Ada class Bus: turunan dari Kendaraan, punya tambahan penumpang.
# Bus override method jalan() → tapi juga memanggil method jalan() dari Kendaraan menggunakan super().
# Tambahkan method muat_penumpang() di Bus.

class Kendaraan:
    def __init__(self, nama):
        self.nama = nama

    def jalan(self):
        print(f"{self.nama} sedang berjalan di jalan umum")


class Bus(Kendaraan):
    def __init__(self, nama, penumpang):
        super().__init__(nama)
        self.penumpang = penumpang

    
    def jalan(self):
        super().jalan()
        print(f"{self.nama} membawa {self.penumpang} penumpang")

    
    def muat_penumpang(self, jumlah):
        self.penumpang += jumlah
        print(f"{jumlah} penumpang naik ke {self.nama}. Total: {self.penumpang}")

transjakarta = Bus("Transjakarta", 20)
transjakarta.jalan()
transjakarta.muat_penumpang(5)









# 🎯 Kasus: Sistem Kepegawaian Perusahaan
# Buatlah sistem kelas untuk menggambarkan struktur berikut:
# 👇 Ketentuan:
# Buat class Pegawai
# Atribut: nama, gaji_pokok
# Method: tampilkan_info() → menampilkan nama dan gaji pokok
# Method: hitung_gaji() → kembalikan nilai gaji pokok

# Buat class Manajer yang turunan dari Pegawai
# Tambahkan atribut: tunjangan
# Override method hitung_gaji() → kembalikan gaji pokok + tunjangan
# Tambahkan method beri_bonus() yang menampilkan pesan "Bonus diberikan kepada [nama]"

# Buat class Programmer yang turunan dari Pegawai
# Tambahkan atribut: jumlah_project
# Override method hitung_gaji() → gaji pokok + (jumlah_project × 500_000)
# Tambahkan method tambah_project() → menambah jumlah project


class Pegawai:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def tampilkan_info(self):
        print(f"Nama Pegawai: {self.nama}, Gaji Pegawai: Rp {self.gaji_pokok}")

    def hitung_gaji(self):
        print(f"Rp {self.gaji_pokok}")
    

class Manajer(Pegawai):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan
    
    def hitung_gaji(self):
        print(f"Rp {self.gaji_pokok + self.tunjangan}")
    
    def beri_bonus(self):
        print(f"Bonus diberikan kepada {self.nama}")


class Programmer(Pegawai):
    def __init__(self, nama, gaji_pokok, jumlah_project):
        super().__init__(nama, gaji_pokok)
        self.jumlah_project = jumlah_project

    def hitung_gaji(self):
        print(f"Rp {self.gaji_pokok + (self.jumlah_project * 500000)}")
    
    def tambah_project(self, jumlah):
        self.jumlah_project += jumlah
        print(f"Jumlah project menjadi {self.jumlah_project}")

suwarko = Pegawai("Suwarko", 1500000)
suwarko.tampilkan_info()        
suwarko.hitung_gaji()   


munir = Manajer("Munir", 3000000, 200000)
munir.tampilkan_info()
munir.hitung_gaji()
munir.beri_bonus()

raihan = Programmer("Raihan", 2000000, 0)
raihan.tambah_project(2)
raihan.hitung_gaji()