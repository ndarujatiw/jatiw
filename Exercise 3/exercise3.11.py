kota = ["semarang", "solo", "jogja"]

#intentional error
#saya ingin menampilkan kota jogja
#print(kota[3])
#akan menghasilkan :
#Traceback (most recent call last):
  #File "c:\Users\user\Documents\Prokom\alproa\Exercise\Exercise 3\exercise3.11.py", line 2, in <module>
    #print(kota[3])
          #~~~~^^^
#IndexError: list index out of range

#fixed
print(kota[2])