
import requests

link = "http://lenka-niki.blogspot.com/2012/02/bajki-na-dobranoc-kubus-puchatek_24.html"
kubus_raw = requests.get(link)

#kubus_status = kubus_raw.status_code 		#sprawdza status strony
#print ("Status linka:",link , kubus_status)

kubus_text = kubus_raw.text #.encode("utf-8"))

kubus_linie_b = kubus_text.split ("</p>")

#print (kubus_text)

kubus_linie = []
for l in kubus_linie_b:
	#l = l [4:]
	#print ("surowy l =>", l)
	l = l.replace("<p>","")
	kubus_linie.append(l)
	#print ("l po replace => ",l)

#kubus_linie_enumerate = enumerate(kubus_linie)
#print (kubus_linie_enumerate)

koszyk = ["jablka", "maliny", "mango", "agrest"]
for index, x in enumerate(kubus_linie):
	print (index, x)	
	print ()
#print (len(kubus_linie))


