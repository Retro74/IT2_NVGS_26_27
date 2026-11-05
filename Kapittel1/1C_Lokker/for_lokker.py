#print("Hei")
#print("Hei")
#print("Hei")
#print("Hei")
#print("Hei")
#

#print(type(range(5)))
#for i in range(2, 11, 2):
#    print(i)

#import time
#for i in range(10, 0 , -1):
#    print(i)
#    time.sleep(0.5)

#print("GO")
#print(i)

#tekst = input("Skriv en kort tekst: ")

#for tegn in tekst:
#    print(tegn)


#passord = input("Skriv inn ett passord du bruker: ")
#har_stor_bokstav = False
#har_liten_bokstav = False
#har_tall = False
#har_tegn = False
#er_riktig_lengde = len(passord)>=8
#har_mellomrom = False
#
#for tegn in passord:
#    if tegn.isupper():
#        har_stor_bokstav= True
#    elif tegn.islower():
#        har_liten_bokstav=True
#    elif tegn.isdigit():
#        har_tall = True
#    else: 
#        if tegn == " ":
#            har_mellomrom = True
#        har_tegn = True
#
#if (har_stor_bokstav and
#    har_liten_bokstav and
#    har_tegn and
#    har_tall and
#    not har_mellomrom and
#    er_riktig_lengde):
#    print("Passordet er sterkt")
#else:
#    print("Passordet er ikke sterkt")
#    if not har_stor_bokstav:
#        print("Passordet mangler bruk av stor bokstav")
#    if not har_liten_bokstav:
#        print("Passordet mangler bruk av liten bokstav")
#    if not har_tall:
#        print("Passordet mangler bruk av tall")
#    if not har_tegn:
#        print("Passordet mangler bruk av spesialtegn")
#    if har_mellomrom:
#        print("Du har brukt mellomrom, som ikke er tillat")
#    if not er_riktig_lengde:
#        print("Passordet er for kort.")
#
#
#

#elever = ["Ola", "Eli", "Per", "Pål"]
#for elev in elever:
#    print(elev)


#Nestede løkker, tabell
for i in range(1,10):
    print("|", end="")
    for j in ["A", "B", "C", "D"]:
        print(f" {i}-{j} |", end="")
    print()
