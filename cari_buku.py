from daftar_buku import daftar_buku, rak_buku
import detail_buku
import os

def cari():
    while True:
        os.system('cls')
        print("|----Mencari buku-----|")
        daftar_buku(rak_buku)
        detail_buku.data_buku()

        
        pilihan = input("keluar dari menu cari buku? (y/n): ").lower()

        if pilihan == "y":
            break
        
