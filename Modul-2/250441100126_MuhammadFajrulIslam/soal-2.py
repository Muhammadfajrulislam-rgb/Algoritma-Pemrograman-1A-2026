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
print(f"Status Poin       : {status_poin}")