print("Bantulah udin dalam membeli barang-barang perkuliahan, udin hanya punya uang 200k")
uangUdin = 200000
hargaBuku = 25000
hargaPulpen = 8000
hargaFlashdisk = 75000
print("Udin ingin membeli buku, berapa jumlah buku yang udin beli...")
jumlahBuku = int(input())
totalHargaBuku = hargaBuku * jumlahBuku
print("ini total buku = " + str(totalHargaBuku))
print("Udin ingin membeli pulpen, masukkan jumlah pulpen yang di inginkan Udin...")
jumlahPulpen = int(input())
totalHargaPulpen = hargaPulpen * jumlahPulpen
print("ini total pulpen = " + str(totalHargaPulpen))
print("Udin ingin beli flashdik buat menyimpan tugas...")
jumlahFlashdisk = int(input())
totalHargaFlashdisk = hargaFlashdisk * jumlahFlashdisk
print("ini total flashdisk = " + str(totalHargaFlashdisk))
print("Toko sedang mengadakan promo nih...")
totalSeluruhHarga = totalHargaBuku + totalHargaPulpen + totalHargaFlashdisk
print("ini total tanpa diskon = " + str(totalSeluruhHarga))
diskon = totalSeluruhHarga * 0.1
totalSetelahDiskon = totalSeluruhHarga - diskon
print("Total setelah mendapat diskon 10% = " + str(totalSetelahDiskon))
print("Tapi ada PAJAK PERTAMBAHAN NILAI(PPN) sebesar 11%")
totalPpn = totalSetelahDiskon * 11 / 100
totalHargaSetelahPajak = totalSetelahDiskon + totalPpn
print("Yang Perlu Udin Bayar Adalah = " + str(totalHargaSetelahPajak))
hargaAkhir = uangUdin - totalHargaSetelahPajak
print("Untuk Sisa Uang Udin = Rp" + str(hargaAkhir))
