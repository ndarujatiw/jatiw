pengguna_saat_ini = ['ndaru', 'jati', 'SITI', 'joko', 'admin']
pengguna_baru = ['Ndaru', 'JatI', 'siti', 'dimas', 'eka']


pengguna_saat_ini_lower = [user.lower() for user in pengguna_saat_ini]

for user_baru in pengguna_baru:
    if user_baru.lower() in pengguna_saat_ini_lower:
        print(f"Maaf, username '{user_baru}' sudah digunakan. Silakan masukkan username baru.")
    else:
        print(f"Username '{user_baru}' tersedia!")