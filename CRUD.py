import sqlite3

def create_table():
    connection = sqlite3.connect("matakuliah.db")
    cursor = connection.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matakuliah (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kode TEXT NOT NULL,
            nama TEXT NOT NULL,
            sks INTEGER NOT NULL
        )
    ''')

    connection.commit()
    connection.close()


def tambah_matakuliah(kode, nama, sks):
    connection = sqlite3.connect("matakuliah.db")
    cursor = connection.cursor()
  
   
    cursor.execute('''
        INSERT INTO matakuliah (kode, nama, sks)
        VALUES (?, ?, ?)
    ''', (kode, nama, sks))

    connection.commit()
    connection.close()
  

def tampilkan_semua_matakuliah():
    connection = sqlite3.connect("matakuliah.db")
    cursor = connection.cursor()


    cursor.execute('SELECT * FROM matakuliah')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()

def update_matakuliah(kode, new_nama, new_sks):
    connection = sqlite3.connect("matakuliah.db")
    cursor = connection.cursor()


    cursor.execute('''
        UPDATE matakuliah
        SET nama = ?, sks = ?
        WHERE kode = ?
    ''', (new_nama, new_sks, kode))

    connection.commit()
    connection.close()


def hapus_matakuliah(kode):
    connection = sqlite3.connect("matakuliah.db")
    cursor = connection.cursor()

  
    cursor.execute('DELETE FROM matakuliah WHERE kode = ?', (kode,))

    connection.commit()
    connection.close()


create_table()


tambah_matakuliah('MK001', 'Matematika Teknik', 3)
tambah_matakuliah('MK002', 'Teknologi Komputer', 3)
tambah_matakuliah('MK003', 'Logika Matematika', 3)


print("Daftar Mata Kuliah:")
tampilkan_semua_matakuliah()

update_matakuliah('MK002', 'Teknologi Komputasi', 4)

print("\nDaftar Mata Kuliah setelah Update:")
tampilkan_semua_matakuliah()

hapus_matakuliah('MK003')

print("\nDaftar Mata Kuliah setelah Hapus:")
tampilkan_semua_matakuliah()