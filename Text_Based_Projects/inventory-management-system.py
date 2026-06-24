# Data toko
nama_barang = ["Premium Case", "Tempered Glass", "Cable Organizer"]
stok_barang = [10, 15, 20]
harga_barang = [50000, 25000, 15000]

print("--- Selamat Datang di Jonathan Store ---")

while True:
    print("\nMENU TOKO:")
    print("1. Lihat Stok & Harga")
    print("2. Tambah Stok Barang")
    print("3. Keluar dari Program")
    
    pilihan = input("Pilih menu (1/2/3): ")
    
    if pilihan == "1":
        print("\n=== DAFTAR BARANG ===")
        for i in range(len(nama_barang)):
            print(f"{i+1}. {nama_barang[i]} | Stok: {stok_barang[i]} | Harga: Rp{harga_barang[i]}")
            
    elif pilihan == "2":
        print("\n=== TAMBAH STOK ===")
        for i in range(len(nama_barang)):
            print(f"{i+1}. {nama_barang[i]}")

        nomor_pilihan = int(input("Masukkan nomor barang yang mau ditambah stoknya: "))
        
        indeks = nomor_pilihan - 1 
        
        tambah = int(input("Mau tambah berapa stok? "))
        
        stok_barang[indeks] = stok_barang[indeks] + tambah
        print(f"Berhasil! Stok {nama_barang[indeks]} sekarang menjadi {stok_barang[indeks]}")
        
    elif pilihan == "3":
        print("Terima kasih sudah menggunakan program ini. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid, coba lagi!")