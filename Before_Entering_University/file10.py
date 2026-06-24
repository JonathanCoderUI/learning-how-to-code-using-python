# 🕵️‍♂️ Tantangan Logika "Ujian Masuk Asrama"
# Bayangkan kamu diminta membuat sistem otomatis untuk menentukan harga tiket masuk wahana bermain
# berdasarkan umur pengunjung dengan ketentuan berikut:
# Umur kurang dari atau sama dengan 5 tahun -> Tiket Gratis (Rp0).
# Umur kurang dari 17 tahun -> Tiket Anak-anak (Rp25.000).
# Di luar kondisi tersebut (umur 17 tahun ke atas) -> Tiket Dewasa (Rp50.000).

umur = int(input("Berapa umur kamu saat ini: "))

if int(umur) >= 17:
    print("Tiket Dewasa (Rp50.000)")
elif int(umur) >= 6:
    print("Tiket Anak-anak (Rp25.000)")
else:
    print("Tiket Gratis (Rp0)")