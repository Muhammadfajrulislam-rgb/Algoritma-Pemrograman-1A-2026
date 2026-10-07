<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="sKrasny"/>
        <attribute name="authors" value="Budi"/>
        <attribute name="about" value="Program menentukan status sKrasny dari kode 3 digit"/>
        <attribute name="saved" value="2026-10-06 05:47:46 PM"/>
        <attribute name="created" value="2026-10-06 17:44:00"/>
        <attribute name="edited" value="2026-10-06 17:44:00"/>
        <attribute name="edited" value="cjtERVNLVE9QLVNDS0dIR1E7MjAyNi0xMC0wNjswNTo0Nzo0NiBQTTsxOzI2MTI="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="kode" type="Integer" array="False" size=""/>
            <declare name="digit1" type="Integer" array="False" size=""/>
            <declare name="digit2" type="Integer" array="False" size=""/>
            <declare name="digit3" type="Integer" array="False" size=""/>
            <declare name="pelacakAwal" type="Integer" array="False" size=""/>
            <declare name="pelacakTahap1" type="Integer" array="False" size=""/>
            <declare name="nilaiAkhir" type="Integer" array="False" size=""/>
            <declare name="status" type="String" array="False" size=""/>
            <declare name="siklus" type="String" array="False" size=""/>
            <output expression="&quot;=== SISTEM sKrasny ===&quot;" newline="True"/>
            <output expression="&quot;Masukkan kode rahasia 3 digit:&quot;" newline="True"/>
            <input variable="kode"/>
            <assign variable="digit1" expression="kode / 100"/>
            <assign variable="digit2" expression="(kode / 10) mod 10"/>
            <assign variable="digit3" expression="kode mod 10"/>
            <output expression="&quot;Digit pertama = &quot; &amp; digit1" newline="True"/>
            <output expression="&quot;Digit kedua = &quot; &amp; digit2" newline="True"/>
            <output expression="&quot;Digit ketiga = &quot; &amp; digit3" newline="True"/>
            <assign variable="pelacakAwal" expression="digit1 * digit3"/>
            <output expression="&quot;Nilai pelacak awal = &quot; &amp; pelacakAwal" newline="True"/>
            <if expression="digit2 mod 2 = 1">
                <then>
                    <assign variable="pelacakTahap1" expression="pelacakAwal + 25"/>
                </then>
                <else>
                    <assign variable="pelacakTahap1" expression="pelacakAwal - digit2"/>
                </else>
            </if>
            <output expression="&quot;Nilai pelacak setelah tahap pertama = &quot; &amp; pelacakTahap1" newline="True"/>
            <if expression="pelacakTahap1 mod 3 = 0">
                <then>
                    <assign variable="nilaiAkhir" expression="pelacakTahap1 / 3"/>
                </then>
                <else>
                    <assign variable="nilaiAkhir" expression="pelacakTahap1 * 2"/>
                </else>
            </if>
            <output expression="&quot;Nilai pelacak setelah tahap kedua (nilai akhir) = &quot; &amp; nilaiAkhir" newline="True"/>
            <if expression="nilaiAkhir &gt; 50">
                <then>
                    <assign variable="status" expression="&quot;Kategori A&quot;"/>
                </then>
                <else>
                    <if expression="nilaiAkhir &gt; 20">
                        <then>
                            <assign variable="status" expression="&quot;Kategori B&quot;"/>
                        </then>
                        <else>
                            <assign variable="status" expression="&quot;sKrasny Ditolak&quot;"/>
                        </else>
                    </if>
                </else>
            </if>
            <output expression="&quot;Status sKrasny = &quot; &amp; status" newline="True"/>
            <if expression="nilaiAkhir mod 2 = 0">
                <then>
                    <assign variable="siklus" expression="&quot;Siklus Genap&quot;"/>
                </then>
                <else>
                    <assign variable="siklus" expression="&quot;Siklus Ganjil&quot;"/>
                </else>
            </if>
            <output expression="siklus" newline="True"/>
        </body>
    </function>
</flowgorithm>

while True:
    input_belanja = input("Masukkan total belanja awal (Rp): ").strip()
    
    if input_belanja == "":
        print("Peringatan: Input tidak boleh kosong.\n")
        continue
        
    try:
        total_awal = int(input_belanja)
        if total_awal < 0:
            print("Peringatan: Total belanja tidak boleh bernilai negatif.\n")
            continue
    except ValueError:
        print("Peringatan: Tolong jangan input dengan teks atau kalimat karena yang diminta disini adalah berupa angka.\n")


if total_awal % 100000 == 0:
    diskon = 1.0  
elif total_awal % 50000 == 0:
    diskon = 0.50 
elif total_awal % 10000 == 0:
    diskon = 0.20 
elif total_awal >= 200000:
    diskon = 0.10 
else:
    diskon = 0.0  

total_akhir = int(total_awal - (total_awal * diskon))

status_poin = "Poin Bertambah" if total_akhir > 0 else "Tidak Ada Poin"

print("\n--- STRUK BELANJA KOPERASI NDESO ---")
print(f"Total belanja awal: Rp{total_awal}")
print(f"Total harga akhir : Rp{total_akhir}")
print(f"Status Poin       : {status_poin}")while True:
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
print(f"Status Pompa Air : {status_pompa}")while True:
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