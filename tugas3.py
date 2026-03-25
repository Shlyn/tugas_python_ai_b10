print("\n")
print("---Variabel dan Tipe Data---")

#String Variable
nama = "Shelina" 

#Bolean Variable
pelajar = True

#Integer Variable
umur_sekarang = 21
umur_lima_tahun_lalu = umur_sekarang - 5

#Float Variable
tinggi_meters = 1.58
tinggi_sentimeter = tinggi_meters * 100

#List Variable
list_warna = ["biru", "hijau", "merah", "kuning pastel", "magenta"]
warna_favorit = list_warna[3]

print("Nama Saya:", nama)
print("Saya seorang pelajar:", pelajar)
print("Tinggi saya adalah", tinggi_sentimeter, "cm.")
print("Warna favorit saya adalah", warna_favorit)
print("Sekarang saya berumur", umur_sekarang, "tahun. 5 tahun yang lalu, saya berumur", umur_lima_tahun_lalu, "tahun.")


print("\n")
print("---Manipulasi String---")
#String Variable
nama = "Shelina"

#Menghitung panjang string
panjang_nama = len(nama)

#Mengubah huruf menjadi besar
nama_uppercase = nama.upper()

#Mengubah huruf menjadi kecil
nama_lowercase = nama.lower()

print("Nama saya adalah", nama)
print("Panjang nama saya", panjang_nama, "karakter.")
print("Nama saya dalam huruf besar adalah", nama_uppercase)
print("Nama saya dalam huruf kecil adalah", nama_lowercase)


print("\n")
print("---Operasi Matematika---")

#Lingkaran
diameter = 10
radius = diameter / 2
pi = 3.14

keliling = 2 * pi * radius
luas = pi * radius ** 2

print("Keliling lingkaran adalah", keliling)
print("Luas lingkaran adalah", luas)


print("\n")
print("---List dan Akses Elemen---")

#List 5 item.
list_buah = ["apel", "jeruk", "pisang", "mangga", "anggur"]
print("List awal:", list_buah)
print("Elemen ke-2:", list_buah[1]) 

list_buah.remove("pisang")  # Menghapus item menggunakan nama
print("List setelah menghapus 'pisang':", list_buah)

list_buah.append("kiwi")  # Menambahkan item
print("List setelah menambahkan 'kiwi':", list_buah)

list_buah.pop(0)  # Menghapus item menggunakan index
print("List setelah menggunakan pop:", list_buah)


print("\n")
print("---User Input---")

# Contoh: "Halo, nama saya Budi dan umur saya 20 tahun."
nama = input("Masukkan nama Anda: ")
umur = input("Masukkan umur Anda: ")
status = input("Apakah Anda seorang pelajar? (ya/tidak): ")

print("Halo, nama saya", nama,", umur saya", umur, "tahun dan saya seorang pelajar:", status)
