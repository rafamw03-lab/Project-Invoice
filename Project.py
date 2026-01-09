print("PT. SAMPLE SARANA ABADI")
print("Ruko Graha Arteri Mas")
print("Jl. Panjang Blok 101 No.1, Jakarta 12223")
print("Phone : (021) 58305578")
print("="*70)
print("INVOICE")
print("No Invoice   : 00000145")
print("Tanggal      : 11 Februari 2013")
print("Customer     : SAMPLE INDONESIA, PT")
print("Payment Term : Cash / Tunai")
print("="*70)

print("="*40)
print("Kode   Nama Barang     Harga")
print("A1     RAM             35000")
print("B1     CPU             60000")
print("C1     GPU             50000")
print("D1     FAN             20000")
print("="*40)


nama_barang = []
qty = []
harga = []
subtotal = []

jumlah_item = int(input("Masukkan jumlah barang: "))

for i in range(jumlah_item):
    print(f"\nBarang ke-{i+1}")

    kode = input("Kode barang [A1/B1/C1/D1]: ").upper()
    jumlah = int(input("Jumlah          : "))

    if kode == "A1":
        nama = "RAM"
        hrg = 35000
    elif kode == "B1":
        nama = "CPU"
        hrg = 60000
    elif kode == "C1":
        nama = "GPU"
        hrg = 50000
    elif kode == "D1":
        nama = "FAN"
        hrg = 20000
    else:
        print("Kode barang salah!")
        

    nama_barang.append(nama)
    qty.append(jumlah)
    harga.append(hrg)
    subtotal.append(jumlah * hrg)

print("\n" + "="*70)
print("No  Nama Barang        Jumlah     Harga        Subtotal")
print("="*70)

total = 0
for i in range(len(nama_barang)):
    print(f"{i+1:<3} {nama_barang[i]:<18} {jumlah[i]:<10} {harga[i]:<12} {subtotal[i]}")
    total += subtotal[i]

print("="*70)


diskon = 0
pajak = total * 0.1
grand_total = total - diskon + pajak

print(f"Gross Total     : Rp {total}")
print(f"Diskon          : Rp {diskon}")
print(f"Pajak 10%       : Rp {int(pajak)}")
print("="*70)
print(f"NET TOTAL       : Rp {int(grand_total)}")
print("="*70)

print("Transfer Via:")
print("BCA - IDR")
print("A/C : 164-800-3321")
print("A/N : PT. SAMPLE SARANA ABADI")
print("="*70)
print("Terima kasih atas kepercayaan Anda")
