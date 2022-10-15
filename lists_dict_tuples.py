dzien = "Sunday"
dzisiaj = "Monday"

#list = [1,2,3,4,5,6,7]
#doctionary = {"klucz": "wartosc1","wartosc2" }
#tuple = ()

days_of_week = [
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
]
print (days_of_week)


weekend = [
	"Saturday",
	"Sunday",
]
print (weekend)
print ()
print ()

#sprawdza czy dzien jest w liscie days_of_week
if dzien == dzisiaj:
	print ("2a. Tak dzisiaj jest", dzisiaj)

elif dzien in days_of_week:
	print ("2b. Today is working day")
 
#sprawdza czy dzien jest w liscie weekend
elif dzien in weekend:
	print ("2c. Today is a weekend")
else:
	print ("2d. Input data is wrong")
