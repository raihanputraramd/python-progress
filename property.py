# class Mahasiswa:
#     def __init__(self, nama, nilai):
#         self.nama = nama
#         self.__nilai = nilai

    
#     @property
#     def nilai(self):
#         return self.__nilai
    
#     @nilai.setter
#     def nilai(self, value):
#         if 0 <= value <= 100:
#             self.__nilai = value
#         else:
#             print('Nilai harus diantara 0 - 100')

# mhs = Mahasiswa("Raihan", 80)
# print(mhs.nilai) 

# mhs.nilai = 95
# print(mhs.nilai)

# mhs.nilai = 150


# Soal 1
class Suhu:
    def __init__(self, celcius):
        self._celcius = celcius
    

    # Lengkapi property getter/setter untuk celcius
    @property
    def celcius(self):
        return self._celcius
    

    @celcius.setter
    def celcius(self, value):
        self._celcius = value

    
    @property
    def fahrenheit(self):
        return self._celcius * 9/5 + 32


s = Suhu(25)
print(s.celcius)
print(s.fahrenheit)

s.celcius = 30
print(s.fahrenheit)


# Soal 2
class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self._nilai = nilai

    
    @property
    def nilai(self):
        return self._nilai
    
    @nilai.setter
    def nilai(self, value):
        if 0 <= value <= 100:
            self._nilai = value
        else:
            print("Nilai Tidak Valid!")

m = Mahasiswa("Raihan", 70)
print(m.nilai)

m.nilai = 110
print(m.nilai)