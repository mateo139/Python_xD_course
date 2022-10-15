import requests

link = "https://zajecia-programowania-xd.pl/kubus_puchatek"
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



for i, l in enumerate(kubus_linie):
	if "Kubus" in l:
		print (i, l)	

print (len(kubus_linie))


