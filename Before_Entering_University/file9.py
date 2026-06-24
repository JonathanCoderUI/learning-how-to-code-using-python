nama = input("Masukkan nama kamu: ")
tahun_lahir = int(input("Masukkan tahun lahir kamu: "))
print("Halo " + nama + ", selamat datang di dunia CyberSecurity")
print(f"Kamu lahir di tahun {tahun_lahir}")

umur = int(input("Masukkan umur kamu: "))
if umur >= 17:
    print("kamu sudah masuk ke kategori Dewasa!")
else:
    print("Kamu masih anak-anak!")

nilai = int(input("Masukkan nilai ulangan kamu: "))
if nilai >= 85:
    print("Nilai kamu: A (Luar Biasa!)")
elif nilai >= 70:
    print("Nilai kamu: B (Bagus!)")
elif nilai >= 55:
    print("Nilai kamu: C (Cukup, tingkatkan lagi)")
else:
    print("Nilai kamu: E (Kamu harus mengulang kelas)")