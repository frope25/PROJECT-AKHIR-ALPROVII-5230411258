import sqlite3
koneksi = sqlite3.connect('hewan.db')
kursor  = koneksi.cursor()

#Select All
kursor.execute("SELECT SUM(jml_skrg) FROM HEWAN")

total = kursor.fetchone()[0]

print('DATA HEWAN')
print('='*50)
print(f"TOTAL POPULASI HEWAN LANGKA SAAT INI : {total}")
print("-"*50)
print("-"*50)
koneksi.close()