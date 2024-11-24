import os

# Data akun dan chipset
akun = {"admin": {"password": "admin321", "role": "ADMIN"}}
chipsetdata = {
    "A11 Bionic": {"Release Year": 2017, "Cores": 6, "Process": "10nm"},
    "A12 Bionic": {"Release Year": 2018, "Cores": 6, "Process": "7nm"},
    "A13 Bionic": {"Release Year": 2019, "Cores": 6, "Process": "7nm+"},
    "A14 Bionic": {"Release Year": 2020, "Cores": 6, "Process": "5nm"},
    "A15 Bionic": {"Release Year": 2021, "Cores": 6, "Process": "5nm"},
    "A16 Bionic": {"Release Year": 2022, "Cores": 6, "Process": "4nm"},
}

# Fungsi utilitas
def clearscreen():
    """Membersihkan layar untuk tampilan lebih rapi."""
    os.system("cls" if os.name == "nt" else "clear")

def garispemisah():
    """Mencetak garis pemisah untuk memperindah tampilan."""
    print("=" * 50)

def tekanlanjut():
    """Memberikan waktu jeda agar user bisa membaca sebelum melanjutkan."""
    input("\nTekan [Enter] untuk melanjutkan...")

# Fungsi utama
def welcomeMessage():
    """Menampilkan menu utama."""
    clearscreen()
    garispemisah()
    print("         SELAMAT DATANG DI SISTEM CHIPSET")
    garispemisah()
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("4. Total Chipset Data")
    garispemisah()

def cekusername(username):
    """Memeriksa apakah username sudah terdaftar."""
    return username in akun

def tampilkanchipset():
    """Menampilkan data chipset secara iteratif."""
    if not chipsetdata:
        print("\nData chipset masih kosong.")
    else:
        garispemisah()
        print("               DATA CHIPSET")
        garispemisah()
        for nama_chipset, spesifikasi in chipsetdata.items():
            print(f"\nChipset: {nama_chipset}")
            for key, value in spesifikasi.items():
                print(f"  {key}: {value}")
        garispemisah()

def totalchipsetdata():
    """Menghitung jumlah chipset yang tersedia."""
    return len(chipsetdata)

def managechipsetdata(role):
    """Mengelola data chipset berdasarkan peran pengguna."""
    while True:
        clearscreen()
        garispemisah()
        print("             MENU PENGELOLAAN CHIPSET")
        garispemisah()
        print("1. Lihat semua data chipset")
        if role == "ADMIN":
            print("2. Tambah data chipset")
            print("3. Ubah data chipset")
            print("4. Hapus data chipset")
        print("5. Kembali ke menu utama")
        garispemisah()

        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan == "1":  # Lihat semua data chipset
            clearscreen()
            if not chipsetdata:
                print("\nData chipset masih kosong.")
            else:
                tampilkanchipset()
            tekanlanjut()

        elif pilihan == "2" and role == "ADMIN":  # Tambah data chipset
            clearscreen()
            print("       TAMBAH DATA CHIPSET")
            garispemisah()
            nama_chipset = input("Masukkan nama chipset baru: ").strip()
            if nama_chipset in chipsetdata:
                print("Chipset sudah terdaftar. Tidak dapat menambahkan duplikat.")
            else:
                try:
                    tahun_rilis = int(input("Masukkan tahun rilis (contoh: 2023): ").strip())
                    cores = int(input("Masukkan jumlah core (contoh: 6): ").strip())
                    proses = input("Masukkan teknologi proses (contoh: 5nm): ").strip()
                    chipsetdata[nama_chipset] = {
                        "Release Year": tahun_rilis,
                        "Cores": cores,
                        "Process": proses,
                    }
                    print(f"Data chipset '{nama_chipset}' berhasil ditambahkan.")
                except ValueError:
                    print("Input tidak valid. Pastikan tahun dan core berupa angka.")
            tekanlanjut()

        elif pilihan == "3" and role == "ADMIN":  # Ubah data chipset
            clearscreen()
            print("       UBAH DATA CHIPSET")
            garispemisah()
            nama_chipset = input("Masukkan nama chipset yang ingin diubah: ").strip()
            if nama_chipset in chipsetdata:
                try:
                    print(f"Data lama chipset '{nama_chipset}': {chipsetdata[nama_chipset]}")
                    tahun_rilis = int(input("Masukkan tahun rilis baru: ").strip())
                    cores = int(input("Masukkan jumlah core baru: ").strip())
                    proses = input("Masukkan teknologi proses baru: ").strip()
                    chipsetdata[nama_chipset] = {
                        "Release Year": tahun_rilis,
                        "Cores": cores,
                        "Process": proses,
                    }
                    print(f"Data chipset '{nama_chipset}' berhasil diperbarui.")
                except ValueError:
                    print("Input tidak valid. Pastikan tahun dan core berupa angka.")
            else:
                print("Chipset tidak ditemukan.")
            tekanlanjut()

        elif pilihan == "4" and role == "ADMIN":  # Hapus data chipset
            clearscreen()
            print("       HAPUS DATA CHIPSET")
            garispemisah()
            if not chipsetdata:
                print("Tidak ada data chipset yang dapat dihapus.")
            else:
                nama_chipset = input("Masukkan nama chipset yang ingin dihapus: ").strip()
                if nama_chipset in chipsetdata:
                    del chipsetdata[nama_chipset]
                    print(f"Data chipset '{nama_chipset}' berhasil dihapus.")
                else:
                    print("Chipset tidak ditemukan.")
            tekanlanjut()

        elif pilihan == "5":  # Kembali ke menu utama
            print("Kembali ke menu utama.")
            tekanlanjut()
            main()
            break

        else:  # Penanganan input salah
            print("Pilihan tidak valid. Silakan coba lagi.")
            tekanlanjut()

def proses_login():
    """Proses login pengguna."""
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()
    if cekusername(username) and akun[username]["password"] == password:
        print("Login berhasil!")
        tekanlanjut()
        managechipsetdata(akun[username]["role"])
        return True
    else:
        print("Username atau password salah.")
        tekanlanjut()
        return False

def prosesregister():
    """Proses registrasi pengguna baru."""
    username_baru = input("Masukkan username baru: ").strip()
    if cekusername(username_baru):
        print("Username sudah terdaftar.")
    else:
        password_baru = input("Masukkan password baru: ").strip()
        akun[username_baru] = {"password": password_baru, "role": "USER"}
        print("Registrasi berhasil.")
    tekanlanjut()

# Program utama
def main():
    salah = 0
    while salah < 3:
        welcomeMessage()
        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan == "1":
            clearscreen()
            if proses_login():
                break
            else:
                salah += 1
        elif pilihan == "2":
            clearscreen()
            prosesregister()
        elif pilihan == "3":
            clearscreen()
            garispemisah()
            print("Terima kasih telah menggunakan program ini!")
            garispemisah()
            break
        elif pilihan == "4":
            clearscreen()
            garispemisah()
            print(f"Total Chipset Data: {totalchipsetdata()}")
            garispemisah()
            tekanlanjut()
        else:
            print("Pilihan tidak valid.")
            tekanlanjut()

    if salah >= 3:
        print("Anda telah gagal login sebanyak 3 kali. Program selesai.")

if __name__ == "__main__":
    main()
