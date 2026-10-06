while True:
    input_pin = input("Masukkan 3 digit PIN: ").strip()
    if input_pin == "":
        print("Peringatan: Input tidak boleh kosong.\n")
        continue
    try:
        pin = int(input_pin)
        if pin < 0:
            print("Peringatan: PIN tidak boleh bernilai negatif.\n")
            continue
        break
    except ValueError:
        print("Peringatan: Tolong jangan input dengan teks atau kalimat karena yang diminta disini adalah berupa angka.\n")

while True:
    input_jam = input("Masukkan jam kedatangan (0-23): ").strip()
    if input_jam == "":
        print("Peringatan: Input tidak boleh kosong.\n")
        continue
    try:
        jam = int(input_jam)
        if jam < 0 or jam > 23:
            print("Peringatan: Jam tidak valid (harus 0-23) dan tidak boleh negatif.\n")
            continue
        break
    except ValueError:
        print("Peringatan: Tolong jangan input dengan teks atau kalimat karena yang diminta disini adalah berupa angka.\n")


digit_1 = pin // 100
digit_2 = (pin // 10) % 10
digit_3 = pin % 10

if pin % 5 == 0:
    if jam < 12:
        status_akses = "Garasi Pagi Terbuka"
    else:
        status_akses = "Garasi Malam Terbuka, Lampu Dinyalakan"
elif pin % 2 == 0:
    if (digit_1 + digit_3) == digit_2:
        status_akses = "Garasi VIP Terbuka Khusus Bos"
    else:
        status_akses = "Kode Genap Ditolak, Alarm Berbunyi!"
else:
    status_akses = "Akses Ditolak Sepenuhnya"

status_cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

print("\n--- LOG AKSES GARASI MARKAS ---")
print(f"Digit 1: {digit_1}, Digit 2: {digit_2}, Digit 3: {digit_3}")
print(f"Status Pintu Garasi: {status_akses}")
print(f"Status Kamera CCTV : {status_cctv}")