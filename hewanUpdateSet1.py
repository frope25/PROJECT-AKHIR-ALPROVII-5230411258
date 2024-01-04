import sqlite3
koneksi = sqlite3.connect('hewan.db')
kursor  = koneksi.cursor()

#Select All
jmlSkrgUpdate = 900
idHewan = 1
kursor.execute(f"UPDATE HEWAN SET jml_skrg = {jmlSkrgUpdate} WHERE id_hewan = {idHewan}")
koneksi.commit()

if kursor.rowcount > 0:
    print(f"Data Hewan dengan id {idHewan} berhasil di update")
else :
    print(f"TIdak ada Data Hewan dengan id {idHewan}")
koneksi.close()