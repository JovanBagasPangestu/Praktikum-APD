usn = "jovan bagas pangestu"
pw = "71"

salah = 1
while salah <= 3:
    login = input ("Apakah Anda ingin login? ")
    if login == "tidak":
        break
    else:
        username = input ("username: ")
        password = input ("password: ")
        if username == usn and password == pw:
            print("Login Berhasil")

            print("Welcome to Body Mass Index (BMI)")
            print("Masukkan tinggi Anda dalam satuan km")
            print("contoh: tinggi Anda 1.55 m, masukkanlah angka 0.00155 km")
            TINGGIBADANkm = float(input("Masukkan tinggi Anda: "))
            TINGGIBADANm = TINGGIBADANkm * 1000
            print(F"Tinggi badan Anda {TINGGIBADANm:.2f} m ")
            print("Masukkan berat badan Anda dalam satuan mg")
            print("contoh: berat badan Anda 55 kg, masukkanlah angka 55000000 mg (berat badan x 1.000.000)")
            BERATBADANmg = float(input("Masukkan berat badan Anda: "))
            BERATBADANkg = BERATBADANmg / 1000000
            print(f"Berat badan Anda adalah {BERATBADANkg:.2f} kg")
            bmi = BERATBADANkg / (TINGGIBADANm ** 2)
            if bmi < 18.5:
                print(f"Skor BMI Anda adalah {bmi:.2f}")
                print("Berat badan Anda kurang (underweight)")
            elif bmi < 24.9:
                print(f"Skor BMI Anda adalah {bmi:.2f}")
                print("Berat badan Anda normal ")
            elif bmi < 29.9:
                print(f"Skor BMI Anda adalah {bmi:.2f}")
                print("Berat badan Anda berlebih (overweight)")
            else:
                print(f"Skor BMI Anda adalah {bmi:.2f}")
                print("Anda tergolong Obesitas")
            break
        else:
            print(f"Login Anda gagal sebanyak {salah} kali")
            print("Anda hanya diberi 3 kali kesempatan untuk Login")         
        salah+=1
if login == "tidak":
    print("Anda tidak memilih untuk Login")
else:
    print("Coba Lagi?")