from database import create_connection

class Pegawai:
    def __init__(self, nomor_pegawai, nama, email, nomor_hp, alamat, divisi_id):
        self.nomor_pegawai = nomor_pegawai
        self.nama = nama
        self.email = email
        self.nomor_hp = nomor_hp
        self.alamat = alamat
        self.divisi_id = divisi_id
    
    @classmethod
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

    def store_pegawai(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO pegawai (nomor_pegawai, nama, email, nomor_hp, alamat, divisi_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (self.nomor_pegawai, self.nama, self.email, self.nomor_hp, self.alamat, self.divisi_id))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = create_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pegawai ORDER BY nama ASC")
        result = cursor.fetchall()
        conn.close()
        return result
    
    @classmethod
    def get_by_nomor_pegawai(cls, nomor_pegawai):
        conn = create_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pegawai WHERE nomor_pegawai = %s", (nomor_pegawai,))
        result = cursor.fetchone()
        conn.close()
        return result
    
    @classmethod
    def update(cls, nomor_pegawai, data):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE pegawai SET nama=%s, email=%s, nomor_hp=%s, alamat=%s, divisi_id=%s WHERE nomor_pegawai=%s
        """, (data['nama'], data['email'], data['nomor_hp'], data['alamat'], data['divisi_id'], nomor_pegawai))
        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, nomor_pegawai):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pegawai WHERE nomor_pegawai = %s", (nomor_pegawai,))
        conn.commit()
        conn.close()
