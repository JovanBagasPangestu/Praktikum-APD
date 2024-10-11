# memanggil

# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])


# menmbahkan

# daftarbuku = {}
# daftarbuku["novel 1"] = "malin kundang"
# daftarbuku[1] = "bulan"
# print(daftarbuku)

# daftarbuku = dict(buku1 = "sasa", buku2 = "sisi", buku3 = "susu")
# print(daftarbuku)

# print(daftarbuku.get("buku2"))
# print(daftarbuku["buku3"])

# nested list

# Biodata = {
# "Nama" : "Aldy Ramadhan Syahputra",
# "NIM" : 2109106079,
# "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" :True,
# "Social Media" : {
# "Instagram" : "@aldyrmdhns_",
# "Discord" : "\'Izanami#6848"
# }
# }


# nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# # for i in nilai:
# #     print(i)

# print(nilai.items())
# for i, j in nilai.items():
# #     print(f" nilai dari {i} itu valuenya adalah: {j}")
# #     print(j)
#     print(i, j)

#tambah

# nilai.update({"strukutur data": 99})
# nilai.update({"Matematika" : 88})
# print(nilai)

#hapus

# trashbin = nilai.pop("Matematika")
# print(nilai)
# print()
# print(type(trashbin))

# del nilai["Fisika"]
# print()
# print(nilai)

# nilai.clear()
# print(nilai)

# print(f"jumlah {len(nilai)}")

# daftarnilai = nilai.copy()
# print(daftarnilai)
# import os

# os.system("cls")
# key = "motor", "mobil", "becak"
# value = 2
# daftarkendaraan = dict.fromkeys(key, value)
# print(daftarkendaraan)

# Musik = {
#     "The Chainsmoker" : ["All we Know", "The Paris"],
#     "Alan Walker" : ["Alone", "Lily"],
#     "Neffex" : ["Best of Me", "Memories"]
# }
# # akses key value dictionary
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     # mengambil nilai dari list
#     for song in j:
#         print(song)
#     print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18, "hobi" : "baca", "nulis", "nyanyi"}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     # for key_a, value_a in value.items():
#     #     print (key_a, " : ", value_a)
#     # print("")
# print (mahasiswa[111]["Nama"]["hobi"][-1])