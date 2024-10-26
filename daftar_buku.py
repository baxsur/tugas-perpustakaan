import os

# tempat menampung semua data buku 
rak_buku = {
    'buku1': {
        'judul': 'Filosofi Teras',
        'penulis': 'Hanry Manampiring',
        'penerbit': 'PT.Kompas Media Nusantara',
        'kategori': 'pengembangan diri',
        'tahun': '2019'
    },
    'buku2': {
        'judul': 'DUNE',
        'penulis': 'Frank Herbert',
        'penerbit': 'Chilton Books',
        'kategori': 'Novel',
        'tahun': '1965'
    }
}

# fungsi yang berguna untuk mencetak daftar buku 
def daftar_buku(rak_buku):
    # untuk mengubah main keys pada rak_buku agar menjadi angka berurutan(buku1:0,buku2:1,dan seterusnya....)
    rak_buku_baru = dict(zip(range(len(rak_buku)), rak_buku.values()))
    os.system('cls')
    print("=======================")
    print("      Daftar Buku")
    print("=======================")

    #untuk memecah setiap main keys dan values pada rak_buku/rak_buku_baru
    for main_keys,detail_buku in rak_buku_baru.items():
        print(f"{main_keys+1}. {detail_buku['judul']}") #

