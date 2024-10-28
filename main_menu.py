from akunAdmin import akunAdmin
from mahasiswa import dashboard_mahasiswa

def main_menu():
    print('''
|-selamat datang di perpustakaan uty-|
|                                    |
|-----0.keluar dari perpustakaan-----|
|-----1.masuk sebagai admin----------|
|-----2.masuk sebagai mahasiswa------|''')
    
    pilihan_akun = input("\nmasuk sebagai admin/mahasiswa? :")#Memasukan Pilihan yang ada didaftar

    #Kondisi untuk memproses semua fitur
    if pilihan_akun == "1":
        # admin.admin()
        akunAdmin()
    elif pilihan_akun == "2":
        dashboard_mahasiswa()
    elif pilihan_akun == "0":
        print("anda telah keluar dari perpustakaan")    
    else:
        print("tolong masukan angka sesuai menu yang ada")

main_menu()
