from daftar_buku import daftar_buku, rak_buku
import cari_buku
import detail_buku
import os

def dashboard_mahasiswa():
    while True:
        os.system('cls')
        print("|-selamat datang pada dashboard mahasiswa-|")
        print("|--apa yang anda ingin lakukan hari ini?--|")
        print("|-0.menu utama         |                  |")
        print("|-1.mencari buku       |                  |")
        print("|-2.mengembalikan buku |                  |")
        pilihan_mahasiswa = input("\nmenu utama/mencari/mengembalikan?,(0/1/2): ")

        if pilihan_mahasiswa == "1":
            cari_buku.cari()
        elif pilihan_mahasiswa == "2":
            detail_buku.mengembalikan()
        elif pilihan_mahasiswa == "0":
            print("kembali ke menu utama")
        else:
            print("mohon masukan angka yang sesuai")

    

dashboard_mahasiswa()