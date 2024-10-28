from tambah_buku import tambah_buku
from remove_buku import remove_buku
import os

def dashboard_admin():
    while True:
        os.system('cls')
        print("="*40)
        print("         DASHBOARD ADMIN")
        print("="*40)
        #Menampilkan pilihan
        print("0. Kembali")
        print("1. Tambah Buku")
        print("2. Hapus Buku")
        dashboard = int(input("Masukan pilihan anda: "))#Memasukan pilihan

        #Konsisi untuk memproses semua fitur
        if dashboard == 1:
            tambah_buku()
        elif dashboard == 2:
            remove_buku()
        elif dashboard == 0:
            break
        else:
            print("Pilihan anda tidak ada dalam daftar!")
        os.system('pause')
