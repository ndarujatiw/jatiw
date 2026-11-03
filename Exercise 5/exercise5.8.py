daftar_pengguna = ['admin', 'ndaru', 'jati', 'siti', 'joko']

for pengguna in daftar_pengguna:
    if pengguna == 'admin':
        print("Halo admin, apakah Anda ingin melihat laporan status?")
    else:
        print(f"Halo {pengguna.title()}, terima kasih sudah login kembali.")