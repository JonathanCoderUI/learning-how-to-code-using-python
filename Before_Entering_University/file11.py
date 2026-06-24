# Soal: https://docs.google.com/document/d/1RBGbj5rfEYC-nTztF7HbINltAB9DnsQrXBjFCZ6E-IU/edit?usp=sharing

Total_Harga = int(input("Berapa Total Harga Belanjaan: "))

if Total_Harga >= 200000:
    Total_Akhir = Total_Harga - 20000
elif Total_Harga >= 100000:
    Total_Akhir = Total_Harga - 5000
else:
    Total_Akhir = Total_Harga

print(f"Total Harga Setelah Diskon: {Total_Akhir}")

Uang = int(input("Masukkan Uang yang Dibayarkan: "))

if Uang >= Total_Akhir:
    print(f"Transaksi Berhasil! Kembalian Anda: Rp{Uang - Total_Akhir}")
else:
    print(f"Transaksi Gagal! Uang Anda kurang Rp{Total_Akhir - Uang}")