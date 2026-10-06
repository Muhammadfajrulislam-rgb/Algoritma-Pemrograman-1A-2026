konsumsiMontor = 40
hargaBensin = 10000
bensinAwal = 1.5

print("Dimas ingin pulang kmapung dan dia belum mengetahui total biaya, bantulah Dimas dalam menghitung total biaya perjalanan")

jarakTempuh = int(input("\nMasukkan Jarak Perjalanan Pulang Kampung Dimas = "))

print("\n==== Jarak Tempuh ====")

pulangPergi = jarakTempuh * 2
print("JARAK PULANG PERGINYA DIMAS = ", pulangPergi, "KM")

print("\n==== Total Bensin Yang Dibutuhkan ====")
kebutuhanBensin = pulangPergi / konsumsiMontor
bensinYangDibeli = kebutuhanBensin - bensinAwal
print("KEBUTUHAAN BENSIN KESELURUHAN =", kebutuhanBensin, "liter")

print("\n==== Bensin Yang Harus Dibeli Di SPBU ====")
bensinYangHarusDibeli = kebutuhanBensin - bensinAwal
print("BENSIN YANG HARUS DI BELI DIMAS = ", bensinYangHarusDibeli, "Liter")


print("\n==== Total Biaya ====")
totalBiaya = bensinYangDibeli * hargaBensin

print("Total Biaya Yang Dibutuhkan Dimas Ketika Pulkam = Rp", totalBiaya)