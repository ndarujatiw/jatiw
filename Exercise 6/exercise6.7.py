# Membuat tiga dictionary terpisah
orang_1 = {
    'nama_depan': 'Ndaru',
    'nama_belakang': 'Wicaksono',
    'umur': 18,
    'kota': 'Surakarta'
}
orang_2 = {
    'nama_depan': 'Ayu',
    'nama_belakang': 'Lestari',
    'umur': 21,
    'kota': 'Yogyakarta'
}
orang_3 = {
    'nama_depan': 'Bima',
    'nama_belakang': 'Sakti',
    'umur': 19,
    'kota': 'Semarang'
}

# Menyimpan dictionary di dalam list (Nesting)
daftar_orang = [orang_1, orang_2, orang_3]

for orang in daftar_orang:
    nama_lengkap = f"{orang['nama_depan']} {orang['nama_belakang']}"
    print(f"\nNama: {nama_lengkap}")
    print(f"Umur: {orang['umur']} tahun")
    print(f"Asal Kota: {orang['kota']}")