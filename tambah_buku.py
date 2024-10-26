def tambah_buku(rak_buku):
    
    # untuk menghitung jumlah buku yang ada pada rak buku,(buku1,buku2,buku3,buku4) = 4
    urutan_buku = len(rak_buku)

    while True:
        # Tambah nomor buku supaya tidak ada yang namanya duplicate
        urutan_buku += 1 # jumlah buku + 1
        buku_ke = "buku" + str(urutan_buku) 

        # Input dari pengguna
        judul = input("Masukkan judul buku: ")
        penulis = input("Masukkan nama penulis: ")
        tahun = input("Masukkan tahun terbit: ")

        # Tambahkan buku baru hasil inputan user ke rak_buku yang berada pada file daftar buku
        rak_buku[buku_ke] = {'judul': judul, 'penulis': penulis, 'tahun': tahun} 

        # Tanya apakah ingin menambah buku lagi
        lanjut = input("Tambah buku lain? (y/n): ").lower()
        if lanjut != 'y':
            break

    # Cetak seluruh isi rak_buku yang baru saja ditambkan
    print("\nDaftar Buku:")
    for key, info_buku in rak_buku.items():
        print(f"{key[-1]}. {info_buku['judul']}")
