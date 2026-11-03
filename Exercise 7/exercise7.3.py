angka = input("Masukkan sebuah angka, dan saya akan memberitahu apakah angka tersebut kelipatan 10 atau bukan: ")
angka = int(angka)

if angka % 10 == 0:
    print(f"\nAngka {angka} adalah kelipatan 10.")
else:
    print(f"\nAngka {angka} bukan kelipatan 10.")