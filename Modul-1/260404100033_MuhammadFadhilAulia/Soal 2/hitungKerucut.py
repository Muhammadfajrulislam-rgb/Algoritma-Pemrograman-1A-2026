r = int(input("Masukkan Jari - Jari Kerucut = "))
t = int(input("Masukkan Tinggi Kerucut = "))

# ==== Proses Perhitungan Volume ====
volume = float(1/3 * 3.14 * r * r * t)

print("\n==== Hasil Volume Dari Kerucut Yang Kamu Masukkan ====")
print("HASIL VOLUME = ", round(volume, 2), "cm³")

# float = real
# round = membulatkan angka - (volume, 2) itu membulatkan 2 angka di belakang koma