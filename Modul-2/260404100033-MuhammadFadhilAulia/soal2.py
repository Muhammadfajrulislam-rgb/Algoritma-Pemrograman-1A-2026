while True:
    try:
        totalBelanjaAwal = int(input("Masukkan total belanja: "))
        if totalBelanjaAwal < 0:
            print("Input tidak sesuai, Masukkan Lagi Total Belanja (Harus Angka Positif)")
            continue
        break
    except ValueError:
        print("Input Tidak Sesuai, Mohon Input kan Angka Saja")

totalHargaAkhir = 0 if totalBelanjaAwal % 100000 == 0 else totalBelanjaAwal * 50 // 100 if totalBelanjaAwal % 50000 == 0 else totalBelanjaAwal * 80 // 100 if totalBelanjaAwal % 10000 == 0 else totalBelanjaAwal * 90 // 100 if totalBelanjaAwal >= 200000 else totalBelanjaAwal

# KETERANGAN PENGECEKAN TOTAL BELANJA IBU SITI
# =================================
# if totalBelanjaAwal % 100000 == 0 ===> pengecekan apakah total belanja ibu siti kelipatan 100.000
# if totalBelanjaAwal % 50000 == 0 ===> pengecekan apakah total belanja ibu siti kelipatan 50.000
# if totalBelanjaAwal % 10000 == 0 ===> pengecekan apakah total belanja ibu siti kelipatan 10.000
# if totalBelanjaAwal >= 200000 ===> pengecekan apakah total belanja ibu siti lebih besar atau sama dengan 200.000
# =================================

print("\n==== TOTAL HARGA YANG HARUS DI BAYAR BU SITI ====")
print("TOTAL HARGA YANG HARUS DI BAYAR:", "Rp", totalHargaAkhir)

print("\n==== STATUS POIN IBU SITI ====")
statusPoin = "Poin Anda Bertambah" if totalHargaAkhir > 0 else "Poin Anda Tidak Bertambah"
print("\nSelamat Ibu Siti, ", statusPoin)