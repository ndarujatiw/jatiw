prompt = "\nBerapa umur Anda?"
prompt += "\n(Ketik 'keluar' jika sudah selesai) "

while True:
    umur = input(prompt)
    
    if umur == 'keluar':
        break
        
    umur = int(umur)
    if umur < 3:
        print("Tiket Anda gratis!")
    elif umur <= 12:
        print("Harga tiket Anda adalah Rp 50.000.")
    else:
        print("Harga tiket Anda adalah Rp 75.000.")