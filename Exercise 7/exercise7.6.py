#Conditional Tests in the While Statement
prompt = "\nMasukkan topping (versi kondisi while): "
topping = ""

while topping != 'keluar':
    topping = input(prompt)
    if topping != 'keluar':
        print(f"Menambahkan {topping}.")
        
#Active Variable
prompt = "\nMasukkan topping (versi flag aktif): "
pesanan_aktif = True

while pesanan_aktif:
    topping = input(prompt)
    
    if topping == 'keluar':
        pesanan_aktif = False
    else:
        print(f"Menambahkan {topping}.")
        
#Break Statement
prompt = "\nMasukkan topping (versi break): "

while True:
    topping = input(prompt)
    
    if topping == 'keluar':
        break
    else:
        print(f"Menambahkan {topping}.")