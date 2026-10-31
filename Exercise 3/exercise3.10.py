gunung = ["Merbabu", "Lawu", "Sumbing", "Sindoro", "Rinjani"]
print(gunung)

#Index
print(f"Saya pernah mendaki ke Gunung {gunung[2]}.")

#Modify
gunung[1]= "Merapi"
print(gunung)

#insert
gunung.insert(3, "Prau")
print(gunung)

#append
gunung.append("Kembang")
print(gunung)

#pop
gunung.pop()
print(gunung)

#delete
del gunung[3]
print(gunung)

#sorted alphabetical sementara(tdk mengubah list)
print(sorted(gunung))
print(sorted(gunung, reverse=True))

#reverse (mengubah list)
gunung.reverse()
print(gunung)

#sort (mengubah list)
gunung.sort()
print(gunung)

#reverse sort (mengubah list)
gunung.sort(reverse=True)
print(gunung)

#len(banyaknya)
print(f"Menurut saya ada {len(gunung)} gunung yang cantik di Indonesia.")