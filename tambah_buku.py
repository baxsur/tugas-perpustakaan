def tambah_buku(rak_buku):
    
    urutan_buku = len(rak_buku)

    while True:
        # Tambah nomor buku supaya tidak ada yang namanya duplicate
        urutan_buku += 1
        buku_ke = "buku" + str(urutan_buku)

        # Input dari pengguna
        judul = input("Masukkan judul buku: ")
        penulis = input("Masukkan nama penulis: ")
        tahun = input("Masukkan tahun terbit: ")

        # Tambahkan buku ke rak_buku
        rak_buku[buku_ke] = {'judul': judul, 'penulis': penulis, 'tahun': tahun}

        # Tanya apakah ingin menambah buku lagi
        lanjut = input("Tambah buku lain? (y/n): ").lower()
        if lanjut != 'y':
            break

    # Cetak seluruh isi rak_buku
    print("\nDaftar Buku:")
    for key, info_buku in rak_buku.items():
        print(f"{key[-1]}. {info_buku['judul']}")
