import requests

def policz_znaki(string):
	dlugosc_stringu = len(string)
	return dlugosc_stringu

link = "https://mamre.pl/Strona/charyzmat/charyzmat-wspolnoty"
kubus_raw = requests.get(link)
kubus_text = kubus_raw.text

link_b = link[:]

print ()
print (link)
print (link_b)
print ()

