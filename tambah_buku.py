from daftar_buku import daftar_buku, rak_buku

def tambah_buku():
    
    # untuk menghitung jumlah buku yang ada pada rak buku,(buku1,buku2,buku3,buku4) = 4
    urutan_buku = len(rak_buku)

    while True:
        # Tambah nomor dibelakang buku supaya tidak ada yang namanya duplikasi
        urutan_buku += 1 # jumlah buku + 1
        buku_ke = "buku" + str(urutan_buku) 

        # Input dari pengguna
        judul = input("Masukkan judul buku: ")
        penulis = input("Masukkan nama penulis: ")
        penerbit = input("masukan penerbit buku: ")
        kategori = input("masukan kategori buku: ")
        tahun = input("Masukkan tahun terbit: ")
        # Tambahkan buku baru hasil inputan user ke rak_buku yang berada pada file daftar buku
        rak_buku[buku_ke] = {
            'judul': judul,
            'penulis': penulis,
            'penerbit' :penerbit,
            'kategori': kategori,
            'tahun': tahun} 

        # Tanya apakah ingin menambah buku lagi
        lanjut = input("Tambah buku lain? (y/n): ").lower() #.lower untuk mengatasi ke autisan dari user bila menginput Y/T 
        if lanjut == 'y':
            print("")
        else:
            break
    
    daftar_buku(rak_buku) # untuk menampilkan daftar buku yang baru di update admin

daftar_buku(rak_buku) # untuk menampilkan daftar buku bawaan 
