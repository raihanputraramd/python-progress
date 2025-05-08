# class Buku:
#     def __init__(self, judul, halaman):
#         self.judul = judul
#         self.halaman = halaman

    
#     def __str__(self):
#         return f"{self.judul} - {self.halaman} halaman"


#     def __len__(self):
#         return self.halaman

# buku1 = Buku("Inception", 148)
# buku2 = Buku("Inception", 150)
# buku3 = Buku("Interstellar", 169)

# print(buku1)

# print(len(buku2))

class Waktu:
    def __init__(self, jam, menit):
        self.jam = jam
        self.menit = menit
    
    
    def __str__(self):
        return f"{self.jam:02d} : {self.menit:02d}"


    def __add__(self, other):
        total_menit = self.menit + other.menit
        total_jam = self.jam + other.jam + total_menit // 60
        sisa_menit = total_menit % 60
        return Waktu(total_jam, sisa_menit)
    
    def __eq__(self, other):
        return self.jam == other.jam and self.menit == other.menit


w1 = Waktu(2, 30)
w2 = Waktu(1, 45)

print(w1)           # Output: 02:30
print(w2)           # Output: 01:45

w3 = w1 + w2
print(w3)           # Output: 04:15

print(w1 == w2)     # Output: False