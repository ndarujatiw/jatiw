kota = {
    'surakarta': {
        'negara': 'indonesia',
        'populasi': '522.364',
        'fakta': 'Terkenal dengan julukan Kota Batik dan slogan "Spirit of Java".'
    },
    'tokyo': {
        'negara': 'jepang',
        'populasi': '13.929.286',
        'fakta': 'Merupakan wilayah metropolitan terpadat di dunia.'
    },
    'paris': {
        'negara': 'prancis',
        'populasi': '2.161.000',
        'fakta': 'Memiliki ikon terkenal Menara Eiffel.'
    }
}

for nama_kota, info_kota in kota.items():
    print(f"\nKota {nama_kota.title()}:")
    print(f"\tNegara: {info_kota['negara'].title()}")
    print(f"\tPopulasi: {info_kota['populasi']} jiwa")
    print(f"\tFakta: {info_kota['fakta']}")