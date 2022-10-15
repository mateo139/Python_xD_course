import requests

link ="https://mamre.pl/Strona/charyzmat/drogowskazy"
kubus_raw = requests.get(link)
kubus_text = kubus_raw.text

dlugosc_textu = len(kubus_text)
print (dlugosc_textu)

ilosc_slow = kubus_text.split()
#print (ilosc_slow)
ilosc_slow_n = len(ilosc_slow)
print (ilosc_slow_n)

div_n = 0
for s in ilosc_slow:
	print (s)
	if s == "</div>":
		div_n += 1
print (div_n)


#kubus_text = kubus_text.replace("/div>", "" )
#kubus_text = kubus_text.replace("</div>", "")
#kubus_text = kubus_text.replace(" ", "@")



#print (kubus_text)
