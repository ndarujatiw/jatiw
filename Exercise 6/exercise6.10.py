angka_favorit = {
    'ndaru': [7, 11, 21],
    'ayu': [12, 24],
    'bima': [8],
    'citra': [24, 48, 96],
    'dimas': [99, 100]
}

for nama, daftar_angka in angka_favorit.items():
    print(f"\nAngka favorit {nama.title()} adalah:")
    for angka in daftar_angka:
        print(f"- {angka}")