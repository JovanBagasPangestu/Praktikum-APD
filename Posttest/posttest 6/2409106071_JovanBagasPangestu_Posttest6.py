akun = {"admin": {"password": "admin321", "role": "ADMIN"}}
kosakata = {}

while True:
    print("\nSelamat datang! Pilih menu:")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan = input("\nMasukkan pilihan: ")
    if pilihan == "1":
        username = input("\nMasukkan username: ")
        password = input("Masukkan password: ")
        if username in akun and akun[username]["password"] == password:
            print("Login berhasil!")
            role = akun[username]["role"]
            while True:
                print("\n1. Lihat kosakata")
                if role == "ADMIN":
                    print("2. Tambah kosakata")
                    print("3. Ubah kosakata")
                    print("4. Hapus kosakata")
                print("5. Logout")
                
                pilihanadmin = input("\nMasukkan pilihan: ")

                if pilihanadmin == "1":
                    if len(kosakata) == 0:
                        print("\nKosakata masih kosong")
                    else:
                        for i, (kata, terjemahan) in enumerate(kosakata.items(), 1):
                            print(f"\nKosakata ke-{i}\nKata: {kata}\nTerjemahan: {terjemahan}")
                elif pilihanadmin == "2" and role == "ADMIN":
                    kata = input("\nMasukkan kata baru: ")
                    if kata in kosakata:
                        print("Kosakata sudah terdaftar")
                    else:
                        terjemahan = input("Masukkan terjemahan: ")
                        kosakata[kata] = terjemahan
                        print("Kosakata berhasil ditambahkan")
                elif pilihanadmin == "3" and role == "ADMIN":
                    kata_lama = input("\nMasukkan kata yang ingin diganti: ")
                    if kata_lama in kosakata:
                        kata_baru = input("Masukkan kata baru: ")
                        terjemahan_baru = input("Masukkan terjemahan baru: ")
                        del kosakata[kata_lama]
                        kosakata[kata_baru] = terjemahan_baru
                        print("Kosakata berhasil diubah")
                    else:
                        print("Kata tidak ditemukan")

                elif pilihanadmin == "4" and role == "ADMIN":
                    if len(kosakata) == 0:
                        print("\nBelum ada kosakata")
                    else:
                        kata_hapus = input("\nMasukkan kata yang ingin dihapus: ")
                        if kata_hapus in kosakata:
                            del kosakata[kata_hapus]
                            print("Kosakata berhasil dihapus")
                        else:
                            print("Kosakata tidak ditemukan")

                elif pilihanadmin == "5":
                    print("\nLogout berhasil.")
                    break
                else:
                    print("\nPilihan Invalid")
        else:
            print("Username atau password salah")
    elif pilihan == "2":
        username_baru = input("\nMasukkan username baru: ")
        if username_baru in akun:
            print("\nUsername sudah terdaftar")
        else:
            password_baru = input("Masukkan password baru: ")
            akun[username_baru] = {"password": password_baru, "role": "user"}
            print("Register berhasil")
    elif pilihan == "3":
        print("\nTerima kasih telah menggunakan program ini!")
        break
    else:
        print("\nPilihan tidak valid.")
