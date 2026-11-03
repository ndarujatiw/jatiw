# Glosarium awal ditambah dengan lima istilah baru
glosarium = {
    'list': 'Struktur data yang menyimpan sekumpulan item berurutan.',
    'tuple': 'Struktur data berurutan yang nilainya tetap (immutable).',
    'boolean': 'Tipe data yang hanya berisi nilai True atau False.',
    'indentasi': 'Spasi awal baris untuk mengelompokkan blok kode.',
    'pep 8': 'Panduan gaya penulisan standar kode Python.',
    'dictionary': 'Struktur data yang menyimpan data dalam pasangan key-value.',
    'string': 'Rangkaian karakter yang diapit tanda kutip.',
    'float': 'Tipe data angka yang memiliki titik desimal.',
    'metode (method)': 'Fungsi yang terikat pada sebuah objek/tipe data.',
    'loop (perulangan)': 'Blok kode yang dieksekusi berulang kali.'
}

# Menggunakan loop untuk mencetak setiap pasangan key dan value
for kata, arti in glosarium.items():
    print(f"{kata.title()}:\n  {arti}\n")