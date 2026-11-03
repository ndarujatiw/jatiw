# Tes untuk kesetaraan dan ketidaksetaraan dengan string
kamera = 'Sony'
print("Apakah kamera == 'Sony'? True")
print(kamera == 'Sony')
print("Apakah kamera != 'Sony'? False")
print(kamera != 'Sony')

# Tes menggunakan metode lower()
awan = 'Altocumulus'
print("\nApakah awan.lower() == 'altocumulus'? True")
print(awan.lower() == 'altocumulus')
print("Apakah awan.lower() == 'Altocumulus'? False")
print(awan.lower() == 'Altocumulus')

# Tes numerik (kesetaraan, ketidaksetaraan, lebih dari, kurang dari, dll)
jumlah_stiker = 7
print("\nApakah jumlah_stiker == 7? True")
print(jumlah_stiker == 7)
print("Apakah jumlah_stiker != 7? False")
print(jumlah_stiker != 7)

print("Apakah jumlah_stiker > 5? True")
print(jumlah_stiker > 5)
print("Apakah jumlah_stiker < 3? False")
print(jumlah_stiker < 3)

print("Apakah jumlah_stiker >= 7? True")
print(jumlah_stiker >= 7)
print("Apakah jumlah_stiker <= 6? False")
print(jumlah_stiker <= 6)

# Tes menggunakan kata kunci 'and' dan 'or'
kapasitas_ram = 4
penyimpanan = 64
print("\nApakah kapasitas_ram == 4 and penyimpanan == 64? True")
print(kapasitas_ram == 4 and penyimpanan == 64)
print("Apakah kapasitas_ram == 8 and penyimpanan == 64? False")
print(kapasitas_ram == 8 and penyimpanan == 64)

print("Apakah kapasitas_ram == 4 or penyimpanan == 128? True")
print(kapasitas_ram == 4 or penyimpanan == 128)
print("Apakah kapasitas_ram == 8 or penyimpanan == 128? False")
print(kapasitas_ram == 8 or penyimpanan == 128)

# Tes apakah sebuah item ada di dalam list (in)
perlengkapan_gitar = ['capo', 'strap lock', 'pick']
print("\nApakah 'capo' ada di dalam list perlengkapan_gitar? True")
print('capo' in perlengkapan_gitar)
print("Apakah 'senar' ada di dalam list perlengkapan_gitar? False")
print('senar' in perlengkapan_gitar)

# Tes apakah sebuah item TIDAK ada di dalam list (not in)
koleksi_baju = ['flanel', 'kaos katun', 'kemeja putih']
print("\nApakah 'jaket' tidak ada di dalam list koleksi_baju? True")
print('jaket' not in koleksi_baju)
print("Apakah 'flanel' tidak ada di dalam list koleksi_baju? False")
print('flanel' not in koleksi_baju)