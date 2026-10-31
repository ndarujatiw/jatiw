Tamu = ["Ahmad", "Jatiw", "Reza"]
#print(f"Halo {Tamu[0]} maukah kamu datang ke rumahku untuk makan malam?")
#print(f"Halo {Tamu[1]} maukah kamu datang ke rumahku untuk makan malam?")
#print(f"Halo {Tamu[2]} maukah kamu datang ke rumahku untuk makan malam?")

tidak_bisa = (Tamu[1])
#print(f"Maaf saya {tidak_bisa} tidak bisa ikut makan malam")

Tamu[1]= "Wicak"
#print(f"Halo {Tamu[0]} maukah kamu datang ke rumahku untuk makan malam?")
#print(f"Halo {Tamu[1]} maukah kamu datang ke rumahku untuk makan malam?")
#print(f"Halo {Tamu[2]} maukah kamu datang ke rumahku untuk makan malam?")

print("Guys, kita kedatangan tamu baru nih!!")
Tamu.insert(0, "Putri")
Tamu.insert(2, "Wok")
Tamu.append("Ted")

#print(f"Halo {Tamu[0]} maukah kamu datang ke rumahku untuk makan malam?")
#print(f"Halo {Tamu[1]} maukah kamu datang ke rumahku untuk makan malam?")
#print(f"Halo {Tamu[2]} maukah kamu datang ke rumahku untuk makan malam?")
#print(f"Halo {Tamu[3]} maukah kamu datang ke rumahku untuk makan malam?")
#print(f"Halo {Tamu[4]} maukah kamu datang ke rumahku untuk makan malam?")
#print(f"Halo {Tamu[5]} maukah kamu datang ke rumahku untuk makan malam?")

print("Maaf guys, aku hanya bisa mengundang 2 orang saja untuk makan malam")
tamu_popped = Tamu.pop()
print(f"Maaf {tamu_popped} aku tidak bisa mengajakmu")
tamu_popped = Tamu.pop()
print(f"Maaf {tamu_popped} aku tidak bisa mengajakmu")
tamu_popped = Tamu.pop()
print(f"Maaf {tamu_popped} aku tidak bisa mengajakmu")
tamu_popped = Tamu.pop()
print(f"Maaf {tamu_popped} aku tidak bisa mengajakmu")

print(f"Halo {Tamu[0]} kamu masih bisa datang ke rumahku.")
print(f"Halo {Tamu[1]} kamu masih bisa datang ke rumahku.")

del Tamu[0]
del Tamu[0]

print("Check Empty List")
print(Tamu)
