import admin
import mahasiswa
import os

def main_menu():
    while True:
        os.system('cls')
        print('''
|-selamat datang di perpustakaan uty-|
|                                    |
|-----0.keluar dari perpustakaan-----|
|-----1.masuk sebagai admin----------|
|-----2.masuk sebagai mahasiswa------|''')
    
        pilihan_akun = input("\nmasuk sebagai admin/mahasiswa? :")

        if pilihan_akun == "1":
            admin.admin()
        elif pilihan_akun == "2":
            mahasiswa.dashboard_mahasiswa()
        elif pilihan_akun == "0":
            print("anda telah keluar dari perpustakaan")    
        else:
            print("tolong masukan angka sesuai menu yang ada")

main_menu()