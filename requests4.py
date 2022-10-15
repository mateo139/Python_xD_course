#importy/biblioteki
import requests #linux: pip3 install requests
		#dokumentacja, wersje itp.

link = "https://fizjo-gabinet.pl/rehabilitacja-w-leczeniu-tezyczki/"
#link = "https://www.mdk.wroc.pl/"
#link = "https://zajecia-programowania-xd.pl/flagi"
flagi_response = requests.get(link)
flagi_text = flagi_response.text

#KOD PONIZSZY DZIALA - ROZWIAZANIE NR 1
#flagi = flagi_text.replace("</p>", "").replace("- ", "").split("<p>")  	#1. podmieniamy za "<p>" -> "", ##2. podmieniamy " -" -> ""
									 	###3.rozbijamy tekst html na liste , wskazujemy "</p>" ze ma byc elementem rozdzielajacym
flagi = flagi_text.split("<p>")

print (flagi)

#f = flagi[111]

#KOD PONIZSZY DZIALA - ROZWIAZANIE NR 2
#for f in flagi:
#	f = f.replace("</p>", "").replace("- ", "").replace("<b>", "").replace("<br>", "").replace("</br>", "")
#	print (f)

#ROZWIAZANIE NR 3
for f in flagi:
	if "- " in f:
		f = f.replace("</p>", "").replace("<b>", "").replace("<br>", "").replace("</br>", "")
		f = f[2:]
		print ("***", f)
	else:
		f = f.replace("</p>", "").replace("<b>", "").replace("<br>", "").replace("</br>", "")
		print ("***", f)


#print (flagi_text)

#listy
#lista = [1, 2, 3, 4]
#lista = ["1", "2", "3", "4"]
#lista = "abcdefg"
#########0123456
#dlugosc_listy =  len(lista)
#print ("To jest dlugosc listy",dlugosc_listy)
#element = lista [5]
#print ("To jest element [5] listy", element)
#petle
#for i in lista:
#	print (i)
