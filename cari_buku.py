from daftar_buku import daftar_buku, rak_buku
import detail_buku
import os


def cari():
    # supaya tidak langsung keluar dari menu daftar buku
    while True:
        os.system('cls')
        print("|----Mencari buku-----|")
        daftar_buku(rak_buku)
        detail_buku.data_buku()
        
        pilihan = input("keluar dari menu cari buku? (y/n): ").lower()
        # keluar dari menu cari buku
        if pilihan == "y":
            break
        
