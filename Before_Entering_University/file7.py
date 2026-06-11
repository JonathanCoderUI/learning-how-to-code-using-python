integer = 2099  # tipe data integer untuk menyimpan angka bulat
word = "Hello"  # tipe data string untuk menyimpan teks

# tipe data string yang berisi angka, bisa diubah ke integer dengan int(string_number)
string_number = "1234"

isHappy = False  # tipe data boolean untuk menyimpan nilai benar atau salah

# tipe data list untuk menyimpan kumpulan data
customer_list = ["John", "Jane", "Doe"]

print(integer)
print(word)
print(isHappy)
print(customer_list)

# buat gabung string dengan integer, harus diubah dulu ke string
print("word" + str(integer))

a = 4
b = 2

# buat operasi matematika dengan variabel
print(a + b)  # penjumlahan
print(a - b)  # pengurangan
print(a * b)  # perkalian
print(a / b)  # pembagian
print(a ** b)  # perpangkatan

# atau operasi matematika bisa juga dengan rumus variabel
pertambahan = a + b
print(pertambahan)
pengurangan = a - b
print(pengurangan)
perkalian = a * b
print(perkalian)
pembagian = a / b
print(pembagian)
perpangkatan = a ** b
print(perpangkatan)

# lanjut belajar logical statement
age = 20
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

isHappy = False
if isHappy:
    print("I am happy")
else:
    print("I am not happy")

# lanjut belajar looping statement
for i in range(5):
    print("Hello", i)

# tapi kalau mau buat hasil hello ga mulai dari 0 melainkan dari 1 bisa gini nih
for i in range(5):
    print("Hello", i + 1)

# bisa juga buat list dengan looping
for name in customer_list:
    print("Customer name:", name)

# kalau fungsi while bisa juga gini
count = 0
while count < 5:
    print("Count is", count) 
    count += 1  # ini sama dengan command count = count + 1

# ada lagi kayak gini
while True:
    user_input = input("Type 'exit' to stop the loop: ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break

# lanjut ke functions
def greet(name):
    print("Hello", name)

input_name = input("Enter your name: ")
greet(input_name)

# atau misal nih mau bikin functions tapi masih belom tau isinya apa, bisa gini nih
def my_function():
    pass  # ini buat placeholder, nanti bisa diisi dengan kode yang sebenarnya

# last mau bahas tentang command try
number = input("Enter a number: ")
try:
    number = int(number)  # coba ubah input ke integer
    print("You entered the number:", number)
except:  # kalau ada error karena input bukan angka
    print("That's not a valid number. Please enter a numeric value.")