print("Halo selamat datang di bioskop!")

def tempat():
    print("Dimanakah kamu ingin menonton?")
    print("1) XXI Empire")
    print("2) XXI Amplaz")
    print("3) XXI JCM")
    pilihan = input("Masukkan pilihanmu: ")
    
    def film():
        print("Mau nonton film apa nih? Ada film: ")
        print("1. Frozen")
        print("2. Keramat")
        print("3. KKN di Desa Penari")
        film = int(input("Pilih nomor film: "))
        if(film > 3):
            print("Pilihan tidak tersedia")
            return 0
    film()

    def layar():
        print("Mau nonton layar bioskop apa: ")
        print("1. Reguler")
        print("2. Dolby almos")
        print("3. Premiere")
        layar = input("Pilih nomor tipe layar: ")
        tiket = input("Berapa banyak tiket? ")
    layar()
    
    def pukul():
        print("Mau nonton pukul berapa: ")
        print("1. 12.35")
        print("2. 14.45")
        print("3. 16.55")
        print("4. 19.05")
        angka = input("Masukkan angka pilihan anda: ")
        if(angka==1):
            print("Oke berhasil, silahkan dinikmati di jam 12.35")
        elif(angka==2):
            print("Oke berhasil, silahkan dinikmati di jam 14.45")
        elif(angka==3):
            print("Oke berhasil, silahkan dinikmati di jam 16.55")
        else:
            print("Oke berhasil, silahkan dinikmati di jam 19.05")
    pukul()
tempat()
