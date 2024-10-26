rak_buku = {}

def daftar_buku():

    # daftar buku bawaan
    rak_buku = {
    'buku1' : {
    'judul':'Filosofi Teras',
    'penulis':'Hanry Manampiring',
    'penerbit':'PT.Kompas Media Nusantara',
    'kategori':'pengembangan diri',
    'tahun':'2019'
    },
    'buku2' : {
    'judul':'DUNE',
    'penulis':'Frank Herbert',
    'penerbit':'Chilton Books',
    'kategori':'Novel',
    'tahun':'1965'
    }
    }
    
    # rak buku baru untuk membuat main keys pada rak buku menjadi angka berurutan(buku1 = 0),(buku2 = 1),dan seterusnya...
    # dengan hal ini urutan pada buku yang ada akan tetap terpertahankan walaupun dihapus atau ditambah
    rak_buku_baru = dict(zip(range(len(rak_buku)), rak_buku.values()))
    
    print("\nDaftar Buku:")
    # untuk mencetak semua daftar buku yang ada pada rak_buku
    for key,info_buku in rak_buku_baru.items():
        print(f"{key+1}.{info_buku['judul']}")    

daftar_buku()
