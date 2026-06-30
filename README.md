# 🐍 Piton IDE

**Piton** adalah bahasa pemrograman berbasis Python yang menggunakan sintaks **Bahasa Indonesia**, namun juga **mendukung kode Python asli (Inggris)**.  
Piton dirancang khusus untuk mempermudah pemula Indonesia dalam belajar logika pemrograman tanpa hambatan bahasa.

Proyek ini bersifat **Open Source** dan berjalan 100% di browser (HTML + Pyodide).

---

## ✨ Fitur Utama

- ✅ **Dual Mode**: Bisa menulis kode dalam Bahasa Indonesia (Piton) atau Bahasa Inggris (Python asli).
- ✅ **Mode Super Singkat**: Cukup tulis `"hello world"` atau `5 + 10`, otomatis jadi perintah `ketik()`.
- ✅ **Terminal Interaktif**: Input langsung di layar terminal (tanpa popup `prompt()` mengganggu).
- ✅ **CodeMirror Editor**: Syntax highlighting, line number, auto-indent.
- ✅ **Sidebar Pintar**: Berisi **Kamus Piton** dan **Mapping Guide** untuk pemula.
- ✅ **Tombol Pintasan**: Salin kode, Bersihkan kode, Jalankan program.
- ✅ **Responsif**: Bisa dipakai di HP, Tablet, dan Laptop.
- ✅ **100% Open Source**: Bisa di-fork, diedit, dan dikembangkan.

---

## 🚀 Cara Menggunakan

### 1. Buka Website
Buka link GitHub Pages berikut:
> `https://fathirthe-founder1.github.io/Piton/`

### 2. Tulis Kode
- Tulis kode di area editor.
- Kamu bisa pakai **Bahasa Indonesia** (Piton) atau **Bahasa Inggris** (Python asli).
- Untuk mencetak teks, bisa pakai:
  - `ketik("Halo")` (Piton)
  - `print("Halo")` (Python asli)
  - Atau cukup tulis `"Halo"` (Mode Super Singkat)

### 3. Jalankan Program
Klik tombol **▶ Jalankan** di pojok kanan atas.  
Hasil akan muncul di layar **Terminal Output** terpisah.

### 4. Kembali ke Editor
Klik tombol **✕ Kembali** untuk menutup terminal dan kembali ke editor.

---

## 📖 Kamus Piton (Bahasa Indonesia → Python)

| Kategori | Piton | Python |
|----------|-------|--------|
| **Input / Output** | `ketik()` | `print()` |
| | `terima()` | `input()` |
| | `buka()` | `open()` |
| | `tutup()` | `close()` |
| | `baca()` | `read()` |
| | `tulis_file()` | `write()` |
| **Fungsi & Kelas** | `buat` | `def` |
| | `kembalikan` | `return` |
| | `wadah` | `class` |
| | `anon` | `lambda` |
| **Logika** | `jika` | `if` |
| | `jikalau` | `elif` |
| | `selain` | `else` |
| **Perulangan** | `selagi` | `while` |
| | `ulangi` | `for` |
| | `henti` | `break` |
| | `lanjut` | `continue` |
| **Tipe Data** | `teks()` | `str()` |
| | `bilangan()` | `int()` |
| | `desimal()` | `float()` |
| | `daftar` | `list` |
| | `kamus` | `dict` |
| | `panjang()` | `len()` |
| | `jenis()` | `type()` |
| | `rentang()` | `range()` |
| **Boolean** | `BENAR` | `True` |
| | `SALAH` | `False` |
| | `KOSONG` | `None` |
| **Operator** | `dan` | `and` |
| | `atau` | `or` |
| | `bukan` | `not` |
| | `dalam` | `in` |
| | `adalah` | `is` |
| **Modul** | `ambil` | `import` |
| | `dari` | `from` |
| | `sebagai` | `as` |
| **Error Handling** | `coba` | `try` |
| | `tangkapi` | `except` |
| | `bersihkan` | `finally` |
| | `lontar` | `raise` |
| **Matematika** | `maks()` | `max()` |
| | `min()` | `min()` |
| | `total()` | `sum()` |
| | `urut()` | `sorted()` |
| **Khusus** | `__nama__` | `__name__` |
| | `__utama__` | `__main__` |

---

## 🧠 Mapping: Mode Super Singkat (Untuk Pemula)

Piton memiliki fitur **Mode Super Singkat** yang memungkinkan kamu menulis kode tanpa perlu mengetik perintah panjang.

### Aturan:
1. Jika sebuah baris hanya berisi **string (teks dalam kutip)** atau **angka**, Piton akan otomatis mengubahnya menjadi `ketik()`.
2. Jika baris mengandung **tanda sama dengan (`=`)**, logika (`jika`), atau perulangan (`selagi`), baris tersebut **tidak akan diubah**.

### Contoh:

| Kode yang Kamu Tulis | Hasil yang Dijalankan |
|----------------------|------------------------|
| `"Halo dunia"` | `ketik("Halo dunia")` |
| `5 + 10` | `ketik(5 + 10)` |
| `nama = "Fathir"` | Tetap sebagai variabel |
| `jika x > 5:` | Tetap sebagai logika |
| `selagi benar:` | Tetap sebagai perulangan |

> ✅ Mode ini sangat membantu pemula yang baru belajar dan belum terbiasa dengan sintaks.

---

## ⚙️ Teknologi yang Digunakan

| Teknologi | Fungsi |
|-----------|--------|
| **HTML + CSS + JS** | Struktur dan tampilan UI |
| **CodeMirror** | Editor kode dengan syntax highlighting |
| **Pyodide** | Menjalankan Python langsung di browser |
| **WebAssembly** | Teknologi di balik Pyodide |
| **GitHub Pages** | Hosting gratis untuk website |

---

## 📁 Cara Mengedit & Mengembangkan

1. **Fork** repositori ini di GitHub.
2. **Clone** ke komputer atau HP kamu.
3. Edit file `index.html` sesuai keinginan.
4. Commit dan push perubahan ke GitHub.
5. GitHub Pages akan otomatis memperbarui website.

---

## 📜 Lisensi

Proyek ini menggunakan lisensi **MIT License**.  
Kamu bebas menggunakan, mengedit, dan menyebarkan kode ini.

---

> **"Mulai dari yang kecil, kirim sesuatu."** — Piton IDE 🐍
> 
> **Dibuat oleh:** [Fathirthe-founder1](https://github.com/Fathirthe-founder1)
