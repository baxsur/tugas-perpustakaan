from daftar_buku import daftar_buku, rak_buku
import os

rak_dipinjam = {}

def data_buku():
    detail = input("\ntekan enter untuk kembali\nketikan judul buku yang ingin anda baca: ")
    os.system('cls')
    
    for main_keys,detail_buku in list(rak_buku.items()):
       
        if detail_buku['judul'].lower() == detail.lower():
            print(f'''judul    : {detail_buku['judul']}
penulis  : {detail_buku['penulis']})
penerbit : {detail_buku['penerbit']}
kategori : {detail_buku['kategori']}
tahun    : {detail_buku['tahun']}
''')
            pinjam = input(f"apakah anda ingin meminjam buku {detail_buku['judul']}, y/n? ").lower()
            os.system('cls')
            if pinjam == "y":
                rak_dipinjam[main_keys] = rak_buku.pop(main_keys)
                daftar_buku(rak_buku)
                print(f"\nanda telah meminjam buku {detail_buku['judul']}")
            else:
                print("")

         
