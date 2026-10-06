while True:
    try:
        pin = int(input("Masukkan PIN anda : "))
        if pin < 0:
            print("Input tidak sesuai, Masukkan Lagi PIN (Harus Angka Positif)")
            continue
        break
    except ValueError:
        print("Input Tidak Sesuai, Mohon Input kan Angka Saja")
while True:
    try:
        jam = int(input("Masukkan jam kedatangan : "))
        if jam < 0:
            print("Input tidak sesuai, Masukkan Lagi Jam (Harus Angka Positif)")
            continue
        break
    except ValueError:
        print("Input Tidak Sesuai, Mohon Input kan Angka Saja")
        
digitPertama = pin // 100
digitKedua = (pin // 10) % 10
digitKetiga = pin % 10

# PROSES HITUNG BOLEH ATAU TIDAK NYA WITO MASUK GARASI
statusWito = "GARASI PAGI TERBUKA" if pin % 5 == 0 and jam < 12 else "GARASI MALAM TERBUKA, LAMPU DINYALAKAN" if jam >= 12 and pin % 5 == 0 else "GARASI VIP TERBUKA KHUSUS BOS" if pin % 2 == 0 and digitPertama + digitKetiga == digitKedua else "KODE GENAP DI TOLAK, ALARM BERBUNYI" if pin % 2 == 0 else "AKSES DITOLAK"

# KETERANGAN PENGECEKAN PIN WITO
# =================================
# if pin % 5 == 0 ====> pengecekan apakah pin wito itu kelipatan 5
# if pin % 2 == 0 and digitPertama + digitKetiga == digitKedua ====> pengecekan apakah pin wito itu genap dan setelah itu apakah hasil digit ke 2 itu sama dengan pertama dan ketiga
# if pin % 2 == 0 =====> itu setelah kualifikasi digit 2 salah, pengecekan apakah hasil salahnya tadi genap atau tidak, KALAU TIDAK GENAP AKSES SEMUA DI TOLAK
# ==================================

print("\n==== STATUS WITO ====")
print("\nStatus Wito adalah : ", statusWito)

print("\n==== STATUS KAMERA CCTV ====")
cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"
print("\nStatus Kamera CCTV adalah : ", cctv)