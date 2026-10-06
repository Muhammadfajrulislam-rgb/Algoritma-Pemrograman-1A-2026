while True:
    try:
        suhu = int(input("Masukkan Suhu Raktor: "))
        if suhu < 0:
            print("Input tidak sesuai, Masukkan Lagi Suhu Raktor (Harus Angka Positif)")
            continue
        break
    except ValueError:
        print("Input Tidak Sesuai, Mohon Input kan Angka Saja")
        
while True:
    try:
        tekanan = int(input("Masukkan Tekanan Raktor: "))
        if tekanan < 0:
            print("Input tidak sesuai, Masukkan Lagi Tekanan Raktor (Harus Angka Positif)")
            continue
        break
    except ValueError:
        print("Input Tidak Sesuai, Mohon Input kan Angka Saja")

print("\n==== STATUS SUHU DAN TEKANAN REAKTOR ====")
# if suhu > 1000 and tekanan > 50:
#     statusReaktor = "MELTDOWN! SEGERA EVAKUASI"
# elif 500 < suhu < 1000:
#     statusReaktor = "BAHAYA SUHU, SEGERA TURUNKAN DAYA"
# elif tekanan > 30:
#     statusReaktor = "SEGERA CEK TEKANAN GAS"
# elif suhu >= 500:
#     statusReaktor = "TEKANAN TIDAK STABIL"
# else:
#     statusReaktor = "REAKTOR BELUM PANAS"
statusReaktor = "MELTDOWN! SEGERA EVAKUASI" if suhu > 1000 and tekanan > 50 else "BAHAYA SUHU, SEGERA TURUNKAN DAYA" if suhu < 1000 and suhu > 500 else "SEGERA CEK TEKANAN GAS" if tekanan > 30 else "TEKANAN TIDAK STABIL" if suhu >= 500 else "REAKTOR BELUM PANAS"
print("Status Reaktor: ", statusReaktor)

print("\n==== STATUS OPERASIOANAL ====")
statusOperasional = "Pompa Normal" if suhu <= 800 else "Pompa Maksimal"
print("Status Operasional: ", statusOperasional)