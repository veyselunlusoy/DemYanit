import sqlite3

DB_PATH = "demya.sqlite3"

def create_database():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 1. Ana Hat Tablosu
    cur.execute("""
    CREATE TABLE IF NOT EXISTS PolnetHatTBL (
        Hat_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Lokasyon TEXT,
        IpAdres TEXT,
        KontrolEt BOOLEAN DEFAULT 1,
        cevapDurumu BOOLEAN DEFAULT 1,
        PingTarihSaat DATETIME,
        Time_MS TEXT,
        TemosNo TEXT
    )
    """)

    # 2. Ping Log Tablosu
    cur.execute("""
    CREATE TABLE IF NOT EXISTS PolnetHatLogTBL (
        Log_Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Hatt_id INTEGER,
        Birim_Lokasyon TEXT,
        IP_Adres TEXT,
        Degisiklik_Zamanı DATETIME,
        TemosNo TEXT,
        Durum TEXT,
        YokBilgisiVerildi BOOLEAN DEFAULT 0,
        YokBilgisiZamanı DATETIME,
        BilgiVerilenKisi TEXT,
        KapaliKalmaSuresi INTEGER
    )
    """)

    # 3. Kontrol Zamanları Logu
    cur.execute("""
    CREATE TABLE IF NOT EXISTS KontrolZamani (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        KontrolZamani DATETIME
    )
    """)

    # 4. E-Posta Bilgilendirme Sistemi (Opsiyonel)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS EmailList (
        Sicil TEXT PRIMARY KEY,
        ADISOYADI TEXT,
        EMAIL TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Tablo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sicil TEXT,
        konu TEXT,
        gonderildi BOOLEAN DEFAULT 0,
        FOREIGN KEY(sicil) REFERENCES EmailList(Sicil)
    )
    """)

    conn.commit()
    conn.close()
    print("Veritabanı ve tablolar başarıyla oluşturuldu.")

if __name__ == "__main__":
    create_database()
