# Soal 1: Pewarisan Sederhana
# Buatlah class Manusia yang memiliki atribut nama, dan method sapa() yang menampilkan Halo, saya [nama].

# Kemudian buat class Mahasiswa yang merupakan turunan dari class Manusia dan tambahkan atribut baru universitas.

# Tambahkan juga method tampilkan_info() untuk menampilkan:

class Manusia:
    def __init__(self, nama):
        self.nama = nama
    
    def sapa(self):
        print(f"Halo, saya {self.nama}")



class Mahasiswa(Manusia):
    def __init__(self, nama, universitas):
        super().__init__(nama)
        self.universitas = universitas

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Universitas: {self.universitas}")


mhs = Mahasiswa("Andi", "Universitas Indonesia")
mhs.sapa()
mhs.tampilkan_info()


# Soal 2: Pewarisan dan Method Tambahan
# Buat class Hewan yang memiliki method bergerak() yang mencetak "Hewan sedang bergerak."

# Buat class Burung yang mewarisi Hewan, dan tambahkan method terbang() yang mencetak "Burung sedang terbang."

# Buat objek elang dari class Burung, lalu panggil kedua method.

class Hewan:
    def bergerak(self):
        print(f"Hewan sedang bergerak")



class Burung(Hewan):
    def terbang(self):
        print(f"Burung Sedang Terbang")


elang = Burung()
elang.bergerak()
elang.terbang()



# Soal 3: Pewarisan dan Konstruktor
# Buat class Akun dengan atribut username dan method login() yang mencetak "User [username] login".

# Buat class AkunPremium yang mewarisi Akun dan tambahkan atribut fitur_premium, serta method akses_premium() yang mencetak:
# "User [username] mengakses [fitur_premium]".

class Akun:
    def __init__(self, username):
        self.username = username


    def login(self):
        print(f"User {self.username} login")



class AkunPremium(Akun):
    def __init__(self, username, fitur_premium):
        super().__init__(username)
        self.fitur_premium = fitur_premium

    
    def akses_premium(self):
        print(f"User {self.username} mengakses {self.fitur_premium}")


akun_vip = AkunPremium("raihan", "VVIP")
akun_vip.login()
akun_vip.akses_premium()