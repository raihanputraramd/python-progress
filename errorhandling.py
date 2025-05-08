# try:
#     angka_pertama = int(input("Masukan Angka pertama: "))
#     angka_kedua = int(input("Masukan Angka kedua: "))

#     hasil = angka_pertama / angka_kedua
# except ZeroDivisionError:
#     print("Tidak bisa membagi dengan nol!")
# except ValueError:
#     print("Input keduanya harus berupa angka")
# else:
#     print(f"Hasil: {hasil}")
# finally:
#     print("Program selesai.")


def kalkulator(angka1, angka2, operasi):
    try:
        angka1 = float(angka1)
        angka2 = float(angka2)

        if operasi == "1":
            hasil = angka1 + angka2
        elif operasi == "2":
            hasil = angka1 - angka2
        elif operasi == "3":
            hasil = angka1 * angka2
        elif operasi == "4":
            hasil = angka1 / angka2
        else:
            raise ValueError("Operasi Tidak Dikenali")

        print(f"Hasil operasi nya adalah: {hasil}")


    except ZeroDivisionError:
        print("Tidak bisa membagi dengan 0")
    except ValueError as e:
        print("Kesalahan: {e}")
    finally:
        print("Program Selesai")


angka1 = input("Masukan Angka Pertama: ")
angka2 = input("Masukan Angka Kedua: ")
print("Pilih Operasi Matematika Dibawah Sesuai dengan nomor nya")
print("1 = '+'")
print("2 = '-'")
print("3 = '*'")
print("4 = '/'")
operasi = input("Pilih Operasi Seusai Nomor: ")

kalkulator(angka1, angka2, operasi)