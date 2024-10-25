# nama = "jopan"
# prent("nama saya adalah", nama)

#syntax error
# if cx < 10:
#     print("x kurang dari 10")
# else:
#     print("x lebih dari 10")

#index error
# harga = (1000,2000,3000)
# print(harga[8])

#atribut error
# umur = 18
# umur.apper()

#import error
# import sigma

#key error
# buku = {
#     "buku1" : "MTK"
#     "buku2" : "IPA"
# }
# print(buku["buku3"])

#name error
# print(a)

#trytry
# try:
#     hargabarang = int(input("masukkan harga barang: "))
#     print(hargabarang)
# except ValueError as e:
#     print(e)
#     print("harus angka wak")
# except Exception:
#     print("salah wak")
# else:
#     print(hargabarang)
# finally:
#     print("nah bener")

# try:
#     nama = input("Hello, what's your name? ")
#     if len(nama) > 5:
#         raise ValueError("Nama tidak boleh lebih dari 5 karakter")
# except ValueError as e:
#     print(e)


# def panggil():
#     try:
#         umur = int(input("masukan umur anda: "))
#     except ValueError:
#         print("umur harus angka")
#         panggil()
#     else:
#         print("umur anda adalah", umur)

# panggil()


# with open("database.txt", "r") as file:
#     konten = file.read()
#     print(konten)

import json

with open("database.json", "r") as file:
    data = json.load(file)
    data.dump("tes")
    print(data)
    data.close()