**Nama**: Elena Sandra Dwi Rahmadani  
**NPM**: 2213020047  
**Kelas**: 3A

Aplikasi ini memungkinkan pengguna untuk mengunggah gambar dan mengonversinya ke dalam format grayscale, biner (hitam-putih), dan warna terindeks.

## Instalasi dan Menjalankan Aplikasi

### 1. Ekstrak Aplikasi
Ekstrak file ZIP ke lokasi yang mudah diakses, seperti Desktop atau direktori `C:\`.

### 2. Buka Folder di VSCode
- Jalankan Visual Studio Code.
- Klik menu `File > Open Folder`, lalu pilih folder hasil ekstrak.

### 3. Buka Terminal
- Klik menu `Terminal > New Terminal`, atau
- Tekan tombol `Ctrl + \`` (tanda backtick di sebelah angka 1 pada keyboard).

### 4. Buat Virtual Environment
```bash
python -m venv venv
```

### 5. Aktifkan Virtual Environment
Sesuaikan dengan jenis terminal yang digunakan:

- PowerShell (Windows):
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

- Command Prompt (Windows):
  ```cmd
  venv\Scripts\activate
  ```

- Git Bash / Bash (Windows/Linux):
  ```bash
  source venv/Scripts/activate
  ```

Jika berhasil, akan muncul nama environment di awal baris terminal, misalnya `(venv)`.

### 6. Install Dependency
```bash
pip install -r requirements.txt
```

### 7. Jalankan Aplikasi
```bash
python app.py
```

### 8. Akses Aplikasi di Browser
Buka browser dan akses alamat berikut:
```
http://127.0.0.1:5000/
```
