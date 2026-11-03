pesanan_sandwich = [
    'pastrami', 'tuna', 'pastrami', 'telur', 
    'ayam panggang', 'pastrami', 'keju leleh'
]
sandwich_selesai = []

print("Maaf, kedai kami kehabisan bahan pastrami hari ini.\n")

# Menghapus semua 'pastrami' dari daftar pesanan menggunakan while
while 'pastrami' in pesanan_sandwich:
    pesanan_sandwich.remove('pastrami')

# Memproses sisa pesanan
while pesanan_sandwich:
    sandwich_saat_ini = pesanan_sandwich.pop()
    print(f"Saya sedang membuat sandwich {sandwich_saat_ini} Anda.")
    sandwich_selesai.append(sandwich_saat_ini)

print("\nSemua pesanan sandwich telah selesai dibuat:")
for sandwich in sandwich_selesai:
    print(f"- Sandwich {sandwich.title()}")