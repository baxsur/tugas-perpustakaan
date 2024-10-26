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
    
    # rak buku baru untuk membuat main keys pada rak buku menjadi angka berurutan(buku1 = 0),(buku2 = 1),dan seterusnya...
    # dengan hal ini urutan pada buku yang ada akan tetap terpertahankan walaupun dihapus atau ditambah
    rak_buku_baru = dict(zip(range(len(rak_buku)), rak_buku.values()))
    
    print("\nDaftar Buku:")
    # untuk mencetak semua daftar buku yang ada pada rak_buku
    for key,info_buku in rak_buku_baru.items():
        print(f"{key+1}.{info_buku['judul']}")    
