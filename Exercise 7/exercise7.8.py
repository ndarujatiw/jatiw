pesanan_sandwich = ['tuna', 'telur', 'ayam panggang', 'keju leleh']
sandwich_selesai = []

# Proses setiap pesanan hingga list pesanan kosong
while pesanan_sandwich:
    sandwich_saat_ini = pesanan_sandwich.pop()
    print(f"Saya sedang membuat sandwich {sandwich_saat_ini} Anda.")
    sandwich_selesai.append(sandwich_saat_ini)

print("\nSemua pesanan sandwich telah selesai dibuat:")
for sandwich in sandwich_selesai:
    print(f"- Sandwich {sandwich.title()}")