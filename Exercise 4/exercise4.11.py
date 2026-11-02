pizzas = ["pepperoni", "New York Style", "Margherita"]
#for pizza in pizzas :
#    print(f"aku suka {pizza} pizza.")
#print("\n Aku sangat suka pizza!")

friend_pizzas = pizzas[:]
pizzas.append("Naples")
friend_pizzas.append("Sisilia")

print("Pizza favorit saya adalah:")
for x in pizzas:
    print(x)
    
print("Pizza favorit teman saya adalah:")
for x in friend_pizzas:
    print(x)