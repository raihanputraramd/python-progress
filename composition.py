# Soal Latihan Composition
# 🔧 Deskripsi:
# Buatlah 2 class:
# 1. Mesin
# Method:
# start() → cetak "Mesin dinyalakan."
# stop() → cetak "Mesin dimatikan."
# 2. Mobil
# Atribut:
# mesin (objek dari class Mesin)
# merek (nama mobil)
# Method:
# nyalakan_mobil() → nyalakan mesin + cetak "Mobil [merek] siap digunakan."
# matikan_mobil() → matikan mesin + cetak "Mobil [merek] dimatikan."

class Mesin:
    def start(self):
        print("Mesin dinyalakan")

        
    def stop(self):
        print("Mesin dimatikan")


class Mobil:
    def __init__(self, merek):
        self.mesin = Mesin()
        self.merek = merek

    def nyalakan_mobil(self):
        self.mesin.start()
        print(f"Mobil {self.merek} siap digunakan")

    
    def matikan_mobil(self):
        self.mesin.stop()
        print(f"Mobil {self.merek} dimatikan")


avanza = Mobil("Toyota Avanza")

avanza.nyalakan_mobil()
avanza.matikan_mobil()
