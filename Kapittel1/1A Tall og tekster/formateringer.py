## Demo av avrunding med f-string samt fixed antall posisjoner
#pi = 3.14
#radius_1 = 4
#radius_2 = 115
#areal_1 = pi * radius_1**2
#areal_2 = pi * radius_2**2

#print(f"Sirkel 1 med {radius_1:5} har areal {areal_1:8.2f}")
#print(f"Sirkel 2 med {radius_2:5} har areal {areal_2:8.2f}")

overskrift = " Norske byer "
by_1 = "Oslo"
by_2 ="Trondheim"
by_3 = "Bergen"
by_4 = "Harstad"
innbygger_1 = 728_000
innbygger_2 = 295_000
innbygger_3 = 218_000
innbygger_4 = 25_000

#Fixed antall posisjoner (Default plassering)
#print(overskrift.center(34,"-"))  #En sentrert overskrift
#print(f"{by_1:10} har {innbygger_1:8} innbyggere")
#print(f"{by_2:10} har {innbygger_2:8} innbyggere")
#print(f"{by_3:10} har {innbygger_3:8} innbyggere")
#print(f"{by_4:10} har {innbygger_4:8} innbyggere")
#print("-"*34, end="\n\n")
#
### Høyre venstre/høyre-justering
#print(f"{by_1:>10} er {innbygger_1:<8} innbyggere")
#print(f"{by_2:>10} er {innbygger_2:<8} innbyggere")
#print(f"{by_3:>10} er {innbygger_3:<8} innbyggere")
#print(f"{by_4:>10} er {innbygger_4:<8} innbyggere")

##Demo med escape-charater for spesialtegn
#print("Han sa: Det \"fint\" vær")
#print("Linje 1: Hallo \nLinje 2: Hei ")

##Kontroll på enden av itskriften
#print("Roger", end=" ")
#print("Mikalsen")

##Tab
#print("Opel \tToyota \tTesla")
#sti = r"C:\\users\\rogmik\\dokumenter"
#sti = r"C:\users\rogmik\dokumenter"
#print(sti)

##Funksjoner for diverse tekst-formatering
tekst = "HeI PÅ deg! 123"
#print(tekst.lower())
#print(tekst.upper())

boktittel = "the hunger games"
#print(boktittel.capitalize())

navn= "nils sivert jensen"
#print(navn.title())

#pi = input(f"Skriv inn tallet for pi: ")
#pi = pi.replace(",", ".")
#pi = pi.replace(",", "")

#pi = float(pi)
#radius = 4

#areal = pi*radius**2
#print(areal)


tekst = "Python er gøy, ikke sant!"
#print(tekst.index("n"))

#print(tekst.find("p"))
#print(tekst.count("p"))

#print(tekst[0]) #Plukker ut tegn på posisjon 0 altså "P"
#print(tekst[5]) #Plukker ut tegn på posisjon 5 altså "n"
#print(tekst[-1]) #Plukker ut tegn på posisjon -1 altså siste tegn "!"
#print(tekst[0:6]) #Plukker ut tegn fra posisjon 0, inntil pos 6, altså "Python"
#print(tekst[:6])  #Plukker ut tegn fra posisjon 0, inntil pos 6, altså "Python"
#print(tekst[20:]) #Plukker ut tegn fra posisjon 20, og ut, altså "sant!"
#print(tekst[::2]) #Plukker ut annen hvert tegn
#print(tekst[::-1]) #Snur hele teksten
print(len(tekst))

import math #Anbefalt
#from math import pi
#print(round(math.pi,5))
#pi_int = int(math.pi)
#print(pi_int)
#print(3+5.2)
#print(5-3)
#print(5*3)
#print(9/7)
#print(3**5) #potens
#print(23%3) #modulus (rest av divisjon)
#print(23//3) #Helltallsdivisjonen
#print((2+3)*5) #Parentes



#tall = input("Skriv inn alder: ").strip()
#if tall.isdigit():
#    tall= int(tall)
#    print(f"Om 5 år er du: {tall + 5}")
#else:
#    print("Du må skrive inn et tall")

#while True:
#    try:
#        alder = int(input("Hvor gammel er du? "))#

#    except ValueError:
#        print("Du må skrive inn ett tall")
        