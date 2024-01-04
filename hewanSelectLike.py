import sqlite3
koneksi = sqlite3.connect('hewan.db')
kursor  = koneksi.cursor()

#Select All
nama = 'B%'
kursor.execute("SELECT * FROM HEWAN WHERE nama_hewan LIKE ?", (nama,))

baris_tabel = kursor.fetchall()

print('DATA HEWAN')
print('='*150)
print("{:<5} {:<30} {:<30} {:<30} {:<30} {:<30}".format("id_hewan","nama_hewan","jenis","asal","jml_skrg","thn_ditemukan"))
print("-"*150)

for baris in baris_tabel:
    print("{:<5} {:<30} {:<30} {:<30} {:<30} {:<30}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))

print("-"*150)
koneksi.close()