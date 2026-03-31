print ("---List---")
my_list = [1, "hello", 3.14, "world", 42, True]

print("Elemen pertama:", my_list[0])
print("Elemen terakhir:", my_list[-1])
print("Slicing [1:4]:", my_list[1:4])

# Lakukan: append(), insert(), extend(), pop(), remove() lalu tampilkan sebelum & sesudah.
print("\nList sebelum append:", my_list)
my_list.append("12.56")
print("List setelah append:", my_list)

print("\nList sebelum insert:", my_list)
my_list.insert(2, "inserted item")
print("List setelah insert:", my_list)

print("\nList sebelum extend:", my_list)
my_list.extend([100, "apaantuh"])
print("List setelah extend:", my_list)

print("\nList sebelum pop:", my_list)
my_list.pop(2)
print("List setelah pop:", my_list)

print("\n")
print ("---Tuple---")
# Tampilkan panjang (len()), akses indeks, dan unpacking (minimal 3 variabel, gunakan *rest bila perlu).
my_tuple = (10, "tuple", 3.14, "mieayam", True)
print("Panjang tuple:", len(my_tuple))
print("Elemen pertama:", my_tuple[0])
print("Elemen ketiga:", my_tuple[2])

a, b, c, *rest = my_tuple 
print("Unpacking:", a, b, c)
print("Sisa elemen:", rest)


print("\n")
print ("---Set---")
# Buat dua set dengan beberapa elemen yang saling tumpang tindih.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

# Tampilkan: union (|), intersection (&), difference (-), symmetric_difference (^).
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# Tunjukkan bahwa duplikat otomatis hilang.
set3 = {1, 2, 2, 3, 3, 3}
print("Set dengan duplikat:", set3)


print("\n")
print ("---Dictionary---")
# Buat dict data mahasiswa: nama, nim, angkatan, kota.
student = {
    "nama": "Shelina",
    "nim": "2331147",
    "angkatan": 2023,
    "kota": "Batam"
}
# Operasi: tambah key baru, ubah nilai key, hapus key.
print("Dictionary awal:", student)
print()
student["jurusan"] = "Informatika"
print("Dictionary setelah tambah key:", student)

student["kota"] = "Bandung"
print("Dictionary setelah ubah nilai:", student)

del student["nim"]
print("Dictionary setelah hapus:", student)

# Tampilkan keys(), values(), items() dan iterasi menampilkan key: value
print()
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print()
print("Iterasi key: value")
for key, value in student.items():
    print(f"{key}: {value}")
    
    
print("\n")
print("---Nested Structures---")
# Buat list berisi ≥ 4 dict (mis. daftar buku: judul, penulis, tahun).

books = [
    {"judul": "Python Programming", "penulis": "Shelina", "tahun": 2020},
    {"judul": "Data Science Handbook", "penulis": "Abidun", "tahun": 2019},
    {"judul": "Machine Learning Basics", "penulis": "Ketrin Masakan", "tahun": 2021},
    {"judul": "Web Development Guide", "penulis": "Justin Timberlake", "tahun": 2018}
]

# Cetak semua judul dengan loop.
print("Daftar Judul Buku:")
for book in books:
    print(book["judul"])

# Filter buku terbit ≥ tahun tertentu menggunakan list comprehension.
target_year = 2020
filtered_books = [
    book for book in books 
    if book["tahun"] >= target_year
    ]

print(f"\nBuku yang terbit setelah {target_year}:")
for book in filtered_books:
    print(f"- {book['judul']} oleh {book['penulis']}")
    
    
print("\n")
print("---Comprehension and Utilities---")

# List comprehension: dari daftar angka 1–20, buat list genap dan list kuadrat.
list_all_numbers = list(range(1, 21))
even_numbers = [x for x in list_all_numbers if x % 2 == 0]
square_numbers = [x ** 2 for x in list_all_numbers]

print("List semua angka:", list_all_numbers)
print("List genap:", even_numbers)
print("List kuadrat:", square_numbers)

# Dict comprehension: mapping {angka: "genap"/"ganjil"} untuk 1–10.
print()
odd_even_dict = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
dict_even = [k for k, v in odd_even_dict.items() if v == "genap"]
dict_odd = [k for k, v in odd_even_dict.items() if v == "ganjil"]

print("Dictionary genap/ganjil:", odd_even_dict)
print("Angka genap:", dict_even)
print("Angka ganjil:", dict_odd)

# Set comprehension: huruf unik (lowercase) dari sebuah kalimat.
print()
sentence = "Halo, Dunia Tipu-tipu!"
unique_letters = {char.lower() for char in sentence if char.isalpha()}
print("Huruf unik:", unique_letters)


print("\n")
print("---Membership Testing---")
# Cek keanggotaan (in) pada list/set.
my_members = ["Adit", "Tolongin", "Dennis", "Sopo", "Shelin", "Jarwo"]
print("List anggota:", my_members)
print("Apakah Adit ada di list?", "Adit" in my_members)

# Gunakan index() atau in untuk melaporkan posisi/keberadaan item secara ringkas.
print()
print("Posisi Sopo dalam list:", my_members.index("Sopo") if "Sopo" in my_members else "Tidak ditemukan")
if "Dennis" in my_members:
    print("Dennis ditolong adit")
else:
    print("Dennis Tidak ditemukan oleh adit")
