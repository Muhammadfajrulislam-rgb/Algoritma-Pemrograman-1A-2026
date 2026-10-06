while True:
    input_suhu = input("Masukkan suhu reaktor (Celcius): ").strip()
    if input_suhu == "":
        print("Peringatan: Input tidak boleh kosong.\n")
        continue
    try:
        suhu = float(input_suhu)
        if suhu < 0:
            print("Peringatan: Suhu tidak boleh bernilai negatif.\n")
            continue
        break
    except ValueError:
        print("Peringatan: Tolong jangan input dengan teks atau kalimat karena yang diminta disini adalah berupa angka.\n")

while True:
    input_tekanan = input("Masukkan tekanan gas (Bar): ").strip()
    if input_tekanan == "":
        print("Peringatan: Input tidak boleh kosong.\n")
        continue
    try:
        tekanan = float(input_tekanan)
        if tekanan < 0:
            print("Peringatan: Tekanan tidak boleh bernilai negatif.\n")
            continue
        break
    except ValueError:
        print("Peringatan: Tolong jangan input dengan teks atau kalimat karena yang diminta disini adalah berupa angka.\n")


if suhu > 1000:
    if tekanan > 50:
        pesan_status = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        pesan_status = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500: 
    if tekanan > 30:
        pesan_status = "Peringatan: Tekanan Tidak Stabil"
    else:
        pesan_status = "Operasi Reaktor Normal"
else:
    pesan_status = "Reaktor Belum Cukup Panas"

status_pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

print("\n--- STATUS SISTEM REAKTOR ---")
print(f"Suhu Terpantau   : {suhu} derajat Celcius")
print(f"Tekanan Terpantau: {tekanan} Bar")
print(f"Peringatan Sistem: {pesan_status}")
print(f"Status Pompa Air : {status_pompa}")