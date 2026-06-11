# hari ini belajar variabel lagi tapi lebih dalem
first_name = "Jonathan"
last_name = "Kana"
full_name = first_name + " " + last_name
print(full_name)
# atau cara lainnya gini nih
full_name = f"{first_name} {last_name}"
print(full_name)
# di dalem {} kita bisa juga buat operasi matematika atau len
len_full_name = f"{first_name} {last_name} memiliki panjang {len(full_name)} karakter"
print(len_full_name)
# kita juga bisa buat operasi matematika di dalem {}
math_operation = f"2 + 3 = {2 + 3}"
print(math_operation)
# lanjut belajar lebih dalam ke string methods
course = "   python for everybody"
print(course.capitalize()) # buat huruf pertama jadi kapital
print(course.upper()) # buat semua huruf jadi kapital
print(course.lower()) # buat semua huruf jadi kecil
print(course.title()) # buat huruf pertama di setiap kata jadi kapital
print(course.strip()) # buat hapus spasi di awal dan akhir string
print(course.replace("python", "java")) # buat ganti kata python jadi java
print(course.replace("p", "j")) # buat ganti semua huruf p jadi j
print(course.find("for")) # buat cari posisi kata for, kalau gak ketemu bakal balik -1
print("for" in course) # buat cek apakah kata for ada di dalam string course
print("pro" not in course) # buat cek apakah kata pro gak ada di dalam string course