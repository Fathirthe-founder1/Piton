from .builtins import KAMUS_INTI

def tampilkan_kamus():
    print("\n" + "="*50)
    print("           KAMUS PITONX (Bahasa Indonesia → Python)")
    print("="*50)
    
    kategori = {
        'INPUT / OUTPUT': ['ketik', 'masukan', 'buka', 'tutup', 'baca', 'tulis'],
        'FUNGSI & KELAS': ['buat', 'kembalikan', 'wadah', 'anon', 'serahkan'],
        'LOGIKA': ['jika', 'jikalau', 'selain', 'pasti'],
        'PERULANGAN': ['selagi', 'ulangi', 'henti', 'lanjut', 'lewat'],
        'TIPE DATA': ['teks', 'bilangan', 'desimal', 'logika', 'daftar', 'peta', 'panjang', 'jenis', 'rentang'],
        'BOOLEAN': ['BENAR', 'SALAH', 'KOSONG'],
        'OPERATOR LOGIKA': ['dan', 'atau', 'bukan', 'dalam', 'adalah'],
        'MODUL & IMPORT': ['impor', 'dari', 'sbg'],
        'ERROR HANDLING': ['coba', 'tangkapi', 'lontar'],
        'VARIABEL & SCOPE': ['umum', 'lokal', 'hapus'],
        'MATEMATIKA': ['maks', 'min', 'total', 'urut', 'abs', 'bulat', 'pangkat'],
        'SPECIAL': ['__nama__', '__utama__']
    }
    
    for cat, kata_list in kategori.items():
        print(f"\n\033[33m{cat}\033[0m")
        for kata in kata_list:
            if kata in KAMUS_INTI:
                print(f"  {kata:<15} → {KAMUS_INTI[kata]}")
    
    print("\n" + "="*50)
