import requests

def policz_znaki (string):
	dlugosc_stringa = len(string)
	return dlugosc_stringa

link = "https://mamre.pl/Strona/"
kubus_raw = requests.get(link)
kubus_text = kubus_raw.text

#1.INDEKSOWANIE
#link_b = link [::-1]

#2.METODY WBUDOWANE
#link_b = link.replace("szukany_znak", "wymieniany_znak")
#link_b = link.lower()
#link_b = link.upper()
#jakis_tekst = "DUZE LITERY"
#link_b = jakis_tekst.lower()

#3.DODAWANIE CIAGOW
#link_b = link[:20] + "          " + link[20:]
#link_b = link[20:] + "          " + link[:20]

#1+2+3
#link_b = link[:30].upper() + "      " + link[10:].upper()

#4. DZIELENIE TEKSTOW
ciag = "Jakis ciag znakow "
link_b = ciag.split()


print (ciag)
print ()
print (link)
print (link_b)
print ()
