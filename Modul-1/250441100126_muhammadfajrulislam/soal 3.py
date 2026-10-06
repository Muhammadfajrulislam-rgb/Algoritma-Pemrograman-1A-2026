# Deklarasi variabel secara statis
jarak_satu_arah = 100  # km
efisiensi_bbm = 40  # 40 km per liter
sisa_bbm = 1.5  # liter
harga_per_liter = 10000  #per liter

# Proses perhitungan
total_jarak = jarak_satu_arah * 2  # (PP)
total_kebutuhan_bbm = total_jarak / efisiensi_bbm
bbm_harus_dibeli = total_kebutuhan_bbm - sisa_bbm
total_biaya = bbm_harus_dibeli * harga_per_liter

# Menampilkan hasil
print("=== RINCIAN PERJALANAN DIMAS ===")
print(f"Total jarak perjalanan PP            : {total_jarak} km")
print(f"Total kebutuhan bahan bakar         : {total_kebutuhan_bbm} liter")
print(f"Bahan bakar yang harus dibeli di SPBU: {bbm_harus_dibeli} liter")
print(f"Total biaya pembelian bahan bakar   : Rp {total_biaya:,.0f}")