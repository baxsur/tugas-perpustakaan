import tambah_buku

rak_buku = {}

def daftar_buku():
    rak_buku = {
    'buku1' : {
    'judul':'habit',
    'penulis':'jarwo',
    'tahun':'2019'
    },
    'buku2' : {
    'judul':'entahlah',
    'penulis':'fufufafa',
    'tahun':'2024'
    }
    }
   
    print("\nDaftar Buku:")
    for key, info_buku in rak_buku.items():
        print(f"{key[-1]}. {info_buku['judul']}")

    tambah_buku.tambah_buku(rak_buku)

daftar_buku()