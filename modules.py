# import math_utils

# from math_utils import kurang

# print(math_utils.tambah(5, 4))

# print(kurang(5, 1))

# from my_package import operasi, pembagian

# print(operasi.tambah(1, 1))
# print(pembagian.bagi(5, 2))

from kalkulator import pengurangan, penjumlahan, pembagian, perkalian

a = 10
b = 4

print("Hasil Tambah: ", penjumlahan.tambah(a, b))
print("Hasil Kurang: ", pengurangan.kurang(a, b))
print("Hasil Kali: ", perkalian.kali(a, b))
print("Hasil Bagi: ", pembagian.bagi(a, b))