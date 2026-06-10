# Fashion Studio ETL Pipeline & Data Integration

Sebuah pipeline data ETL (Extract, Transform, Load) End-to-End yang dirancang untuk melakukan *scraping* data produk dari platform **Fashion Studio**, melakukan pembersihan dan transformasi data secara dinamis, serta memuatnya ke berbagai target penyimpanan: database relasional (**PostgreSQL**), local file (**CSV**), dan cloud spreadsheet (**Google Sheets**) melalui API.

## 📌 Project Overview
Project ini mendemonstrasikan alur kerja rekayasa data (*data engineering*) otomatis yang mengintegrasikan ekstraksi data web dengan sistem penyimpanan multi-channel. Pipeline ini dirancang secara modular dan aman, memisahkan logika utama program dari kredensial sensitif menggunakan variabel lingkungan (*environment variables*).

### 🔑 Fitur Utama
* **Automated Web Scraping:** Pengambilan data produk secara langsung dari target website (`https://fashion-studio.dicoding.dev/`).
* **Multi-Target Ingestion:**
  * **PostgreSQL:** Penyimpanan terstruktur untuk kebutuhan query operasional.
  * **CSV (`products.csv`):** Snapshot data lokal untuk analisis portabel.
  * **Google Sheets API:** Sinkronisasi cloud real-time agar data mudah diakses oleh tim non-teknis.
* **Keamanan Data Terjamin:** Menggunakan integrasi `python-dotenv` sehingga kredensial API dan password database tidak di-hardcode di dalam repositori publik.

---

## 📂 Struktur File Project
Repositori ini memiliki susunan struktur berkas sebagai berikut:

```text
├── tests/                      # Suite pengujian otomatis (Unit & Integration testing)
├── utils/                      # Modul pembantu (Konektor database, scraper, dan cleaner)
├── main.py                     # Skrip utama (Orchestrator) untuk menjalankan pipeline ETL
├── products.csv                # Data produk hasil ekspor lokal dari pipeline
├── requirements.txt            # Daftar library Python dan dependensi project
└── submission.txt.txt          # File token / verifikasi submission project
```
## Setup Virtual Environment 
```
python -m venv venv
venv\Scripts\activate
```

## Instal Dependensi / Library
```
pip install --upgrade pip
pip install -r requirements.txt
```

## Konfigurasi Environment Variables
```
DB_USER=postgres
DB_PASSWORD=isi_dengan_password_postgresql_anda
DB_HOST=localhost
DB_PORT=5432
DB_DATABASE=nama_database_tujuan_anda
```

## Konfigurasi Google Sheets API
```
Agar data hasil scraping bisa otomatis terunggah ke Google Sheets, proyek ini memerlukan file kredensial berupa JSON.

1. Buka Google Cloud Console.
2. Buat proyek baru dan aktifkan Google Sheets API dan Google Drive API.
3. Buatlah sebuah Service Account, lalu unduh kunci akun tersebut dalam format JSON.
4. Ubah nama file JSON yang diunduh tadi menjadi google-sheets-api.json.
5. Pindahkan file tersebut ke dalam root folder proyek ini (sejajar dengan main.py).
6. Langkah Krusial: Buka file Google Sheets Anda di browser, lalu klik tombol Share (Bagikan). Masukkan alamat email Service Account Anda (yang ada di dalam file JSON) sebagai editor agar script Python diberikan izin untuk menulis data.
```
## Eksekusi Pipeline Utama
```
python main.py
```

## Menjalankan Unit Testing
```
pytest tests/
```
