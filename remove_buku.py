from daftar_buku import daftar_buku, rak_buku
import os

rak_dihapus ={}#Dictionary untuk menampung Data buku yang dihapus

def remove_buku():

    while True:
        print("="*40)
        daftar_buku(rak_buku)#Menampilkan daftar judul buku
        print("="*40)
        print("0. Kembali")
        print("1. Hapus Buku")
        pilihan = int(input("Masukan Pilihan Anda: "))#Memilih input yang akan dipilih

        #Kondisi untuk memproses fitu hapus buku
        if pilihan == 1:

            detail = input("ketikan judul buku yang ingin anda hapus : ")#Memasukan Judul buku yang akan dihapus
            os.system('cls')
            
            for main_keys,detail_buku in list(rak_buku.items()):#untuk memecah setiap main keys dan values
                #Kondisi untuk memunculkan Setiap Data buku yang dipihlih, Setiap Data buku ini disimpan di Dictionary rak_buku
                if detail_buku['judul'].lower() == detail.lower():
                    print(f'''judul    : {detail_buku['judul']}
        penulis  : {detail_buku['penulis']})
        penerbit : {detail_buku['penerbit']}
        kategori : {detail_buku['kategori']}
        tahun    : {detail_buku['tahun']}
        ''')
                    #Validasi "Apakah Buku akan dihapus?"
                    hapus = input(f"apakah anda ingin menghapus buku ini {detail_buku['judul']}, y/n? ").lower()
                    os.system('cls') 
                    #Kondisi untuk mengolah buku jika jadi untuk dihapus
                    if hapus == "y":# y melambangkan reaksi YA 
                        rak_dihapus[main_keys] = rak_buku.pop(main_keys)
                        daftar_buku(rak_buku)
                        print(f"\nanda telah menghapus buku {detail_buku['judul']}")
                    else:
                        print("")
        #Kondisi Jika memilih kembali ke menu Admin
        elif pilihan == 0:
            break
        #Statment jika inputan salah
        else:
            print("Pilihan yang anda Masukan tidak didalam daftar!")
        os.system('pause')

