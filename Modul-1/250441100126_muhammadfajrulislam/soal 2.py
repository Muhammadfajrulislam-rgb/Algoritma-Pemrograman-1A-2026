import math

# Menerima input dinamis dari pengguna
r = float(input("Masukkan jari-jari alas kerucut (cm): "))
t = float(input("Masukkan tinggi kerucut (cm): "))

# Menghitung volume kerucut
volume = (1 / 3) * math.pi * (r**2) * t

# Menampilkan hasil perhitungan
print(f"Volume kerucut dengan r = {r} cm dan t = {t} cm adalah: {volume:.2f} cm³")