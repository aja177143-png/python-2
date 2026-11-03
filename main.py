print("=== PROGRAM ARITMATIKA ===")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

tambah = angka1 + angka2
kurang = angka1 - angka2
kali = angka1 * angka2

print("\n=== HASIL ARITMATIKA ===")
print("Penjumlahan :", tambah)
print("Pengurangan :", kurang)
print("Perkalian   :", kali)

if angka2 != 0:
    print("Pembagian   :", angka1 / angka2)
else:
    print("Pembagian   : Tidak bisa dibagi nol")

print("========================")
print("Program selesai")