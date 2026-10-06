digit = [0] * (3)

print("Masukkan Kode Anda = ")
for kode in range(0, 2 + 1, 1):
    print("Kode Ke- " + str(kode) + "= ")
    digit[kode] = int(input())
pelacakAwal = digit[0] * digit[2]
print("Pelacakan Kode Awal = " + str(pelacakAwal))
if digit[1] % 2 == 0:
    pelacak1 = pelacakAwal - digit[1]
else:
    pelacak1 = pelacakAwal + 25
if pelacak1 % 3 == 0:
    pelacak2 = float(pelacak1) / 3
else:
    pelacak2 = pelacak1 * 2
if pelacak2 > 50:
    print("Kategori A")
else:
    if pelacak2 > 20:
        print("Kategori B")
    else:
        print("sKrasny Ditolak")
        if pelacak2 % 2 == 0:
            print("Siklus Genap")
        else:
            print("Siklus Ganjil")
