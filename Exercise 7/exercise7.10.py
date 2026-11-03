respons_liburan = {}
polling_aktif = True

while polling_aktif:
    nama = input("\nSiapa nama Anda? ")
    tempat = input("Jika Anda bisa mengunjungi satu tempat di dunia, ke mana Anda akan pergi? ")
    
    # Menyimpan respons ke dalam dictionary
    respons_liburan[nama] = tempat
    
    # Memeriksa apakah ada orang lain yang ingin merespons
    ulangi = input("Apakah ada orang lain yang ingin merespons polling ini? (ya/tidak) ")
    if ulangi.lower() == 'tidak':
        polling_aktif = False

# Polling selesai, tampilkan hasil
print("\n--- Hasil Polling Liburan Impian ---")
for nama, tempat in respons_liburan.items():
    print(f"{nama.title()} sangat ingin mengunjungi {tempat.title()}.")