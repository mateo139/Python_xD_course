# lista
lista = []
lista = [1, 2, 3]
lista = [1, 2, 3]				#cyfry sa typu integer
koszyk = ["jablko1", "jablko2", "jablko3", "garsc malin"]	#napisy sa typu string

print ("Zaczynam")
# petla
for owoc in koszyk:
	print ("1. Wyjmuje", owoc)
	print ("2. Myje"   , owoc)
	print ("3. Zjadam" , owoc)

	if owoc =="garsc malin":
		continue

	print ("4. Wyrzucam ogryzek po", owoc)
	print ()

print ("Skonczylem")
