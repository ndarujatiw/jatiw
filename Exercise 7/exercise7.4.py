prompt = "\nMasukkan topping pizza yang Anda inginkan:"
prompt += "\n(Ketik 'keluar' untuk mengakhiri pesanan) "

topping = ""
while topping != 'keluar':
    topping = input(prompt)
    
    if topping != 'keluar':
        print(f"Saya akan menambahkan {topping} ke pizza Anda.")