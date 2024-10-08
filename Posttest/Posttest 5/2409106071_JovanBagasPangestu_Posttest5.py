akun = [["admin","admin321","ADMIN"]]
kosakata = []

while True:
    print("\nSelamat datang! Pilih menu:")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan = input("\nMasukkan pilihan: ")
    if pilihan == "1":
        username = input("\nMasukkan username: ")
        password = input("Masukkan password: ")
        login = False
        
        for user in akun:
            if user[0] == username and user[1] == password:
                print("Login berhasil!")
                login = True
                role = user[2]
                break
        else:
            print("Username atau password salah")
            
        if login == True:
            while True:
                print("\n1. Lihat kosakata")
                if role == "ADMIN":
                    print("2. Tambah kosakata")
                    print("3. Ubah kosakata")
                    print("4. hapus kosakata")
                print("5. Logout")
                
                pilihanadmin = input("\nMasukkan pilihan: ")

                if pilihanadmin == "1":
                    if len(kosakata) == 0:
                        print("\nkosakata masih kosong")
                    else:
                        for k in range(len(kosakata)):
                            print(f"\nkosakata ke-{k+1}\nKata : {kosakata[k][0]}\nTerjemahan : {kosakata[k][1]}")

                elif pilihanadmin == "2" and role == "ADMIN":
                    kata = input("\nMasukkan kata baru: ")
                    for k in range(len(kosakata)):
                        if kosakata[k][0] == kata:
                            print("kosakata sudah terdaftar")
                            break
                    else:
                        terjemahan = input("Masukkan terjemahan: ")
                        kosakata.append([kata,terjemahan])
                        print("kosakata berhasil ditambahkan")

                elif pilihanadmin == "3" and role == "ADMIN":
                    kata_lama = input("\nMasukkan kata yang ingin diganti: ")
                    for k in range(len(kosakata)):
                        if kosakata[k][0] == kata_lama:
                            kata_baru = input("Masukkan kata baru: ")
                            terjemahan_baru = input("Masukkan terjemahan baru: ")
                            kosakata[k][0] = kata_baru
                            kosakata[k][1] = terjemahan_baru
                            break
                    else:
                        print("kata tidak ditemukan")

                elif pilihanadmin == "4" and role == "ADMIN":
                    if len(kosakata) == 0:
                        print("\nbelum ada kosakata")
                    else:
                        kata_lama = input("\nMasukkan kata lama yang ingin dihapus: ")
                        for k in range(len(kosakata)):
                            if kosakata[k][0] == kata_lama:
                                del kosakata[k]
                                print("kosakata berhasil dihapus")
                                break
                        else:
                            print("kosakata tidak ditemukan")

                elif pilihanadmin == "5":
                    print("\nLogout berhasil.")
                    break
                else:
                    print("\nPilihan Invalid")

    elif pilihan == "2":
        username_baru = input("\nMasukkan username baru: ")
        akun_ada = False
        for u in akun:
            if u[0] == username_baru:
                akun_ada = True
                break

        if akun_ada == True:
            print("\nUsername sudah terdaftar")
        
        else:
            password_baru = input("Masukkan password baru: ")
            role_baru = "user"
            akun.append([username_baru,password_baru,role_baru])
            print("register berhasil")

    elif pilihan == "3":
        print("\nTerima kasih telah menggunakan program ini!")
        break
    else:
        print("\nPilihan tidak valid.")