from database import create_connection

class Pegawai:
    def __init__(self, nomor_pegawai, nama, email, nomor_hp, alamat, divisi_id):
        self.nomor_pegawai = nomor_pegawai
        self.nama = nama
        self.email = email
        self.nomor_hp = nomor_hp
        self.alamat = alamat
        self.divisi_id = divisi_id

    def create_table(cls):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS divisi (
                divisi_id INT PRIMARY KEY,
                nama_divisi VARCHAR(100) NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pegawai (
                nomor_pegawai INT PRIMARY KEY,
                nama VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                nomor_hp VARCHAR(15) NOT NULL,
                alamat VARCHAR(200) NOT NULL,
                divisi_id INT NOT NULL,
                FOREIGN KEY (divisi_id) REFERENCES divisi(id)
            )
        """)
        conn.close()
