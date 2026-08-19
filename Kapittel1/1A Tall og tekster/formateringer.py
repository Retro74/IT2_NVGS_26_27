## Demo av avrunding med f-string samt fixed antall posisjoner

pi = 3.14
radius_1 = 4
radius_2 = 115
areal_1 = pi * radius_1**2
areal_2 = pi * radius_2**2

print(f"Sirkel 1 med {radius_1:5} har areal {areal_1:8.2f}")
print(f"Sirkel 2 med {radius_2:5} har areal {areal_2:8.2f}")

by_1 = "Oslo"
by_2 ="Trondheim"
by_3 = "Bergen"
by_4 = "Harstad"
innbygger_1 = 728_000
innbygger_2 = 295_000
innbygger_3 = 218_000
innbygger_4 = 25_000

#Fixed antall posisjoner (Default plassering)
print(f"{by_1:10} er {innbygger_1:8} innbyggere")
print(f"{by_2:10} er {innbygger_2:8} innbyggere")
print(f"{by_3:10} er {innbygger_3:8} innbyggere")
print(f"{by_4:10} er {innbygger_4:8} innbyggere")

## Høyre venstrejustering
print(f"{by_1:>10} er {innbygger_1:<8} innbyggere")
print(f"{by_2:>10} er {innbygger_2:<8} innbyggere")
print(f"{by_3:>10} er {innbygger_3:<8} innbyggere")
print(f"{by_4:>10} er {innbygger_4:<8} innbyggere")

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

print(tekst.lower())
print(tekst.upper())

