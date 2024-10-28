from daftar_buku import daftar_buku, rak_buku
import os

rak_dipinjam = {}

def data_buku():
    detail = input("\ntekan enter untuk kembali\nketikan judul buku yang ingin anda baca: ")
    os.system('cls')
    
    # list(rak_buku.items() untuk menghindari masalah saat looping
    for main_keys,detail_buku in list(rak_buku.items()):
        # mencetak detail dari buku yang dipilih user
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
                # menyalin main keys beserta isinya ke dalam rak dipinjam dan menghapus salinannya pada rak buku
                rak_dipinjam[main_keys] = rak_buku.pop(main_keys)
                daftar_buku(rak_buku)
                print(f"\nanda telah meminjam buku {detail_buku['judul']}")
                

def mengembalikan():
    while True:
        os.system('cls')
        # untuk mengubah main keys pada rak_buku agar menjadi angka berurutan(buku1:0,buku2:1,dan seterusnya....)
        rak_buku_dipinjam = dict(zip(range(len(rak_dipinjam)), rak_dipinjam.values()))
        print("===========================")
        print("-Daftar Buku yang dipinjam-")
        print("===========================")

        # main keys = key utama pada rak dipinjam
        # detail buku = value dari main keys
        # detail buku[''] = value dari subkey,['judul'],['penulis'],dll
        for main_keys,detail_buku in rak_buku_dipinjam.items(): # untuk memecah setiap main keys dan values pada rak_dipinjam
            print(f"{main_keys+1}. {detail_buku['judul']}")
            print("===========================")
        
        kembalikan = input("\nmasukan judul buku yang ingin anda kembalikan: ")
        os.system('cls')

        for main_keys,detail_buku in list(rak_dipinjam.items()):
            if detail_buku['judul'].lower() == kembalikan.lower():

                rak_buku[main_keys] = rak_dipinjam.pop(main_keys)

                rak_buku_dipinjam = dict(zip(range(len(rak_dipinjam)), rak_dipinjam.values()))
                print("===========================")
                print("-Daftar Buku yang dipinjam-")
                print("===========================")

                for main_keys,detail_buku in rak_buku_dipinjam.items():
                    print(f"{main_keys+1}. {detail_buku['judul']}")
                    print("===========================")
    
                print(f"\nanda telah mengembalikan buku {detail_buku['judul']}")


        pilihan = input("keluar dari menu cari buku? (y/n): ").lower()
        # keluar dari menu cari buku
        if pilihan == "y":
            break
            
            

