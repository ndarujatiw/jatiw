tempat_favorit = {
    'ndaru': ['gunung merbabu', 'keraton surakarta'],
    'ayu': ['pantai parangtritis', 'malioboro', 'candi prambanan'],
    'dimas': ['raja ampat']
}

for nama, daftar_tempat in tempat_favorit.items():
    print(f"\nTempat favorit {nama.title()} adalah:")
    for tempat in daftar_tempat:
        print(f"- {tempat.title()}")