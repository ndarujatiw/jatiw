bahasa_favorit = {
    'ndaru': 'python',
    'raja': 'c',
    'miya': 'ruby',
    'citra': 'python'
}

# Daftar orang yang harus mengambil polling
daftar_peserta = ['ndaru', 'dimas', 'raja', 'eka', 'miya']

for peserta in daftar_peserta:
    # Memeriksa apakah peserta sudah ada di daftar keys dictionary
    if peserta in bahasa_favorit.keys():
        print(f"Terima kasih {peserta.title()} telah merespons polling kami!")
    else:
        print(f"Halo {peserta.title()}, kami mengundang Anda untuk mengikuti polling bahasa pemrograman.")