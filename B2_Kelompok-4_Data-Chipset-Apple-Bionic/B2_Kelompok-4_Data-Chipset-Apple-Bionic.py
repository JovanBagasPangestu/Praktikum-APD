import os

os.system('cls')

akun = {"admin": {"password": "admin321", "role": "ADMIN"}}
chipset_data = {
    "A11 Bionic": {"Release Year": 2017, "Cores": 6, "Process": "10nm"},
    "A12 Bionic": {"Release Year": 2018, "Cores": 6, "Process": "7nm"},
    "A13 Bionic": {"Release Year": 2019, "Cores": 6, "Process": "7nm+"},
    "A14 Bionic": {"Release Year": 2020, "Cores": 6, "Process": "5nm"},
    "A15 Bionic": {"Release Year": 2021, "Cores": 6, "Process": "5nm"},
    "A16 Bionic": {"Release Year": 2022, "Cores": 6, "Process": "4nm"},
}

def welcome_message():
    os.system('cls')
    print("="*40)
    print("Selamat datang!".center(40))
    print("="*40)
    print("Pilih menu: ")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("4. Total Chipset Data")
    print("="*40)

def cek_username(username):
    return username in akun

def tampilkan_chipset_rekursif(chipset_list, index=0):
    if index < len(chipset_list):
        nama_chipset, spesifikasi = chipset_list[index]
        print(f"\nChipset: {nama_chipset}")
        for key, value in spesifikasi.items():
            print(f"{key}: {value}")
        tampilkan_chipset_rekursif(chipset_list, index + 1)

def total_chipset_data():
    return len(chipset_data)

def tampilan_menu():
    welcome_message()
    pilihan = input("\nMasukkan pilihan: ")
    return pilihan

def proses_login(username, password):
    if cek_username(username) and akun[username]["password"] == password:
        print("Login berhasil!")
        role = akun[username]["role"]
        manage_chipset_data(role)
        return True
    else:
        print("Username atau password salah")
        return False

def manage_chipset_data(role):
    while True:
        os.system('cls')
        print("="*40)
        print("Daftar Pilihan".center(40))
        print("="*40)
        print("1. Lihat data chipset")
        if role == "ADMIN":
            print("2. Tambah data chipset")
            print("3. Ubah data chipset")
            print("4. Hapus data chipset")
        print("5. Logout")
        print("="*40)
        
        pilihanadmin = input("\nMasukkan pilihan: ")
        
        if pilihanadmin == "1":  
            if len(chipset_data) == 0:
                print("\nData chipset masih kosong")
                input("\nTekan untuk kembali ke menu")
            else:
                chipset_list = list(chipset_data.items())
                tampilkan_chipset_rekursif(chipset_list)
                input("\nTekan untuk kembali ke menu")

        elif pilihanadmin == "2" and role == "ADMIN":  
            nama_chipset = input("\nMasukkan nama chipset baru: ")
            if nama_chipset in chipset_data:
                print("Chipset sudah terdaftar")
            else:
                tahun_rilis = input("Masukkan tahun rilis: ")
                cores = input("Masukkan jumlah core: ")
                proses = input("Masukkan teknologi proses: ")
                chipset_data[nama_chipset] = {
                    "Release Year": tahun_rilis,
                    "Cores": cores,
                    "Process": proses,
                }
                print("Data chipset berhasil ditambahkan")

        elif pilihanadmin == "3" and role == "ADMIN":  
            nama_chipset = input("\nMasukkan nama chipset yang ingin diubah: ")
            if nama_chipset in chipset_data:
                tahun_rilis = input("Masukkan tahun rilis baru: ")
                cores = input("Masukkan jumlah core baru: ")
                proses = input("Masukkan teknologi proses baru: ")
                chipset_data[nama_chipset] = {
                    "Release Year": tahun_rilis,
                    "Cores": cores,
                    "Process": proses,
                }
                print("Data chipset berhasil diubah")
            else:
                print("Chipset tidak ditemukan")

        elif pilihanadmin == "4" and role == "ADMIN":
            if len(chipset_data) == 0:
                print("\nBelum ada data chipset")
            else:
                nama_chipset = input("\nMasukkan nama chipset yang ingin dihapus: ")
                if nama_chipset in chipset_data:
                    del chipset_data[nama_chipset]
                    print("Data chipset berhasil dihapus")
                else:
                    print("Chipset tidak ditemukan")

        elif pilihanadmin == "5":  
            print("\nLogout berhasil.")
            break
        else:
            print("\nPilihan Invalid")

salah = 1
while salah <= 3:
    pilihan = tampilan_menu()

    if pilihan == "1":  
        username = input("\nMasukkan username: ")
        password = input("Masukkan password: ")
        if proses_login(username, password):
            break
        else:
            print(f"Percobaan login gagal: {salah}/3")
            salah += 1
            input("\nTekan untuk kembali")

    elif pilihan == "2":  
        username_baru = input("\nMasukkan username baru: ")
        if cek_username(username_baru):
            print("\nUsername sudah terdaftar")
        else:
            password_baru = input("Masukkan password baru: ")
            akun[username_baru] = {"password": password_baru, "role": "user"}
            print("Register berhasil")

    elif pilihan == "3":  
        os.system('cls')
        print("\nTerima kasih telah menggunakan program ini!")
        break

    elif pilihan == "4":  
        total = total_chipset_data()
        if total == 0:
            print("Belum ada data chipset")
            input("\nTekan untuk kembali ke menu")
        else:
            print(f"\nTotal Chipset Data: {total}")
            input("\nTekan untuk kembali ke menu")
    else:
        print("\nPilihan tidak valid.")
        input("\nTekan untuk kembali ke menu")

if salah > 3:
    print("Anda telah gagal login sebanyak 3 kali. Program selesai.")