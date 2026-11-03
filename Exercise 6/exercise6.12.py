kota = {
    'surakarta': {
        'negara': 'indonesia',
        'julukan': 'Kota Bengawan',
        'landmark': ['Keraton Surakarta', 'Pasar Gede', 'Masjid Raya Sheikh Zayed'],
        'populasi': '522.364',
        'fakta': 'Pusat kebudayaan Jawa yang kental.'
    },
    'yogyakarta': {
        'negara': 'indonesia',
        'julukan': 'Kota Pelajar',
        'landmark': ['Tugu Jogja', 'Jalan Malioboro', 'Keraton Yogyakarta'],
        'populasi': '373.589',
        'fakta': 'Daerah istimewa yang masih dipimpin oleh seorang Sultan.'
    }
}

print("=== ENSIKLOPEDIA KOTA ===")
for nama_kota, info in kota.items():
    print(f"\n📍 {nama_kota.upper()} ({info['julukan']})")
    print(f"   Negara     : {info['negara'].title()}")
    print(f"   Populasi   : {info['populasi']} jiwa")
    print(f"   Landmark   : {', '.join(info['landmark'])}")
    print(f"   Tahukah Anda? {info['fakta']}")