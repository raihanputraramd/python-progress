# with open('data.txt', 'r') as file:
#     isi = file.read()
#     print(isi)

# with open("data.txt", 'w') as file:
#     file.write("Ini data baru yang ditulis kedalam file. \n")

# with open("data.txt", "a") as file:
#     file.write("Baris tambahan \n")

# with open("data.txt", "r") as file:
#     for baris in file:
#         print(baris.strip());

with open("catatan.txt", "a") as file:
    file.write("Baris 1 \n")
    file.write("Baris 2 \n")
    file.write("Baris 3 \n")


with open("catatan.txt", "r") as file:
    for baris in file:
        print(baris.strip())