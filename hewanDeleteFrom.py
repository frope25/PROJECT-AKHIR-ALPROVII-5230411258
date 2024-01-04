import sqlite3
koneksi = sqlite3.connect('hewan.db')
kursor  = koneksi.cursor()

#Select All

kursor.execute(f"DELETE FROM HEWAN WHERE jenis = 'Mamalia'")
koneksi.commit()

print('Data Berhasil Dihapus')
koneksi.close()