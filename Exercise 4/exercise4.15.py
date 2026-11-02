#Program 1 (List dipecah agar panjang baris dibawah 80 karakter)
hewan = [
    "kucing", "anjing", "marmut", "burung", "bebek",
    "ayam", "ikan"
    ]

print("\nTiga hewan pertama adalah:")
print(hewan[0:3])

print("\nTiga hewan dari tengah daftar adalah:")
print(hewan[2:5])

print("\nTiga hewan terakhir adalah:")
print(hewan[4:])

#Program 2 (Indentasi standar 4 spasi digunakan dalam loop for)
pizzas = ["pepperoni", "New York Style", "Margherita"]
friend_pizzas = pizzas[:]

pizzas.append("Naples")
friend_pizzas.append("Sisilia")

print("Pizza favorit saya adalah:")
for x in pizzas:
    print(x)
    
print("Pizza favorit teman saya adalah:")
for x in friend_pizzas:
    print(x)
    
#Program 3 (# Baris kosong hanya digunakan untuk memisahkan logika menu asli dari menu yang direvisi.)
menu = ("salad", "salmon", "steak", "pasta", "roti")

print("Menu")
for x in menu:
    print(x)
    
menu = ("ayam", "sup", "steak", "pasta", "roti")

print("Menu Baru")
for x in menu:
    print(x)