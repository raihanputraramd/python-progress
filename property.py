class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.__nilai = nilai

    
    @property
    def nilai(self):
        return self.__nilai
    
    @nilai.setter
    def nilai(self, value):
        if 0 <= value <= 100:
            self.__nilai = value
        else:
            print('Nilai harus diantara 0 - 100')

mhs = Mahasiswa("Raihan", 80)
print(mhs.nilai) 

mhs.nilai = 95
print(mhs.nilai)

mhs.nilai = 150