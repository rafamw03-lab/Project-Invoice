# Program Invoice Python

Program ini digunakan untuk membuat **invoice penjualan sederhana** menggunakan Python.
User dapat memilih barang, memasukkan jumlah, lalu sistem akan menghitung total, pajak, dan grand total.

---

## 📌 Alur Kerja Program

### 1. Menampilkan Header Invoice
Program pertama kali menampilkan:
- Nama perusahaan
- Alamat
- Nomor telepon
- Informasi invoice (nomor, tanggal, customer, metode pembayaran)

---

### 2. Menampilkan Daftar Barang
Program menampilkan tabel barang yang tersedia:

| Kode | Nama Barang | Harga |
|-----|------------|--------|
| A1  | RAM        | 35.000 |
| B1  | CPU        | 60.000 |
| C1  | GPU        | 50.000 |
| D1  | FAN        | 20.000 |

---

### 3. Input Jumlah Barang
User diminta memasukkan:
- Jumlah jenis barang yang dibeli

Program kemudian melakukan perulangan sesuai jumlah tersebut.

---

### 4. Input Data Barang (Loop)
Untuk setiap barang:
1. User memasukkan **kode barang**
2. User memasukkan **jumlah barang**
3. Program mengecek kode barang:
   - Jika **valid**, sistem menentukan nama & harga
   - Jika **tidak valid**, program menampilkan pesan error dan mengulang input (`continue`)
4. Data disimpan ke dalam list:
   - `nama_barang`
   - `qty`
   - `harga`
   - `subtotal`

---

### 5. Menampilkan Tabel Invoice
Setelah semua data dimasukkan, program menampilkan tabel invoice:

- Nomor item
- Nama barang
- Jumlah
- Harga satuan
- Subtotal

Sekaligus menghitung **total belanja**.

---

### 6. Perhitungan Tambahan
Program menghitung:
- Total belanja
- Diskon (saat ini 0)
- Pajak 10%
- Grand total


---

### 7. Menampilkan Ringkasan Pembayaran
Program menampilkan:
- Gross Total
- Diskon
- Pajak
- Net Total
- Informasi rekening pembayaran
- Ucapan terima kasih