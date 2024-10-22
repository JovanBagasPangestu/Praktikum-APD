import os
os.system("cls||clear")

akun = {"admin": {"password": "admin321", "role": "ADMIN"}}
kosakata = {}

def welcome_message():
    print("\nSelamat datang! Pilih menu:")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("4. Total Kosakata")

def cek_username(username):
    return username in akun

def kosakata_rekursif(kosakata_list, terjemahnya=0):
    if terjemahnya < len(kosakata_list):
        kata, terjemahan = kosakata_list[terjemahnya]
        print(f"Kata: {kata}, Terjemahan: {terjemahan}")
        kosakata_rekursif(kosakata_list, terjemahnya + 1)

def Total_Kosakata():
    return len(kosakata)

def Tampilan_menu():
    welcome_message()
    pilihan = input("\nMasukkan pilihan: ")
    os.system("cls||clear")
    return pilihan

def proses_login(username, password):
    if cek_username(username) and akun[username]["password"] == password:
        os.system("cls||clear")
        print("Login berhasil!")
        role = akun[username]["role"]
        manage_vocabulary(role)
    else:
        os.system("cls||clear")
        print("Username atau password salah")

def manage_vocabulary(role):
    while True:
        print("\n1. Lihat kosakata")
        if role == "ADMIN":
            print("2. Tambah kosakata")
            print("3. Ubah kosakata")
            print("4. Hapus kosakata")
        print("5. Logout")
        pilihanadmin = input("\nMasukkan pilihan: ")
        os.system("cls||clear")
        if pilihanadmin == "1": 
            
            if len(kosakata) == 0:
                os.system("cls||clear")
                print("\nKosakata masih kosong")
            else:
                os.system("cls||clear")
                kosakata_list = list(kosakata.items())
                kosakata_rekursif(kosakata_list)

        elif pilihanadmin == "2" and role == "ADMIN":  
            
            kata = input("\nMasukkan kata baru: ")
            if kata in kosakata:
                os.system("cls||clear")
                print("Kosakata sudah terdaftar")
            else:
                terjemahan = input("Masukkan terjemahan: ")
                kosakata[kata] = terjemahan
                os.system("cls||clear")
                print("Kosakata berhasil ditambahkan")

        elif pilihanadmin == "3" and role == "ADMIN":
            kosakata_list = list(kosakata.items())
            kosakata_rekursif(kosakata_list)

            kata_lama = input("\nMasukkan kata yang ingin diganti: ")
            if kata_lama in kosakata:
                kata_baru = input("Masukkan kata baru: ")
                terjemahan_baru = input("Masukkan terjemahan baru: ")
                del kosakata[kata_lama]
                kosakata[kata_baru] = terjemahan_baru
                os.system("cls||clear")
                print("Kosakata berhasil diubah")
            else:
                os.system("cls||clear")
                print("Kata tidak ditemukan")

        elif pilihanadmin == "4" and role == "ADMIN": 
            if len(kosakata) == 0:
                os.system("cls||clear")
                print("\nBelum ada kosakata")
            else:
                kosakata_list = list(kosakata.items())
                kosakata_rekursif(kosakata_list)

                kata_hapus = input("\nMasukkan kata yang ingin dihapus: ")
                if kata_hapus in kosakata:
                    del kosakata[kata_hapus]
                    os.system("cls||clear")
                    print("Kosakata berhasil dihapus")
                else:
                    os.system("cls||clear")
                    print("Kosakata tidak ditemukan")

        elif pilihanadmin == "5":  
            os.system("cls||clear")
            print("\nLogout berhasil.")
            break
        else:
            os.system("cls||clear")
            print("\nPilihan Invalid")

while True:
    
    pilihan = Tampilan_menu()

    if pilihan == "1":  
        username = input("\nMasukkan username: ")
        password = input("Masukkan password: ")
        proses_login(username, password)

    elif pilihan == "2":  
        username_baru = input("\nMasukkan username baru: ")
        if cek_username(username_baru):
            print("\nUsername sudah terdaftar")
        else:
            password_baru = input("Masukkan password baru: ")
            akun[username_baru] = {"password": password_baru, "role": "user"}
            os.system("cls||clear")
            print("Register berhasil")

    elif pilihan == "3":  
        print("\nTerima kasih telah menggunakan program ini!")
        break

    elif pilihan == "4":
        total = Total_Kosakata()
        if total == 0:
            print("Belum ada kosakata")
        else:
            print(f"\nTotal Kosakata: {total}")
    else:
        print("\nPilihan tidak valid.")