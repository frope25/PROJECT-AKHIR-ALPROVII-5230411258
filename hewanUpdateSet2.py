import sqlite3
koneksi = sqlite3.connect('hewan.db')
kursor  = koneksi.cursor()

#Select All
idHewan = 3
kursor.execute(f'UPDATE HEWAN SET asal = "Nusa Tenggara Timur" WHERE id_hewan = {idHewan}')
koneksi.commit()

if kursor.rowcount > 0:
    print(f"Data Hewan dengan id {idHewan} berhasil di update")
else :
    print(f"TIdak ada Data Hewan dengan id {idHewan}")
koneksi.close()