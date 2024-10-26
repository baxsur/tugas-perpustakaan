import tambah_buku

rak_buku = {}

def daftar_buku():

    # daftar buku bawaan
    rak_buku = {
    'buku1' : {
    'judul':'filosofi ambatron',
    'penulis':'jarwo',
    'tahun':'2019'
    },
    'buku2' : {
    'judul':'entahlah',
    'penulis':'fufufafa',
    'tahun':'2024'
    }
    }
    
    # untuk mencetak semua daftar buku yang ada pada rak_buku
    print("\nDaftar Buku:")
    for key, info_buku in rak_buku.items():
        print(f"{key[-1]}. {info_buku['judul']}")