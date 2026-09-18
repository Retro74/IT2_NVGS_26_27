biler = [
    ["Toyota", "Yaris", 2022, 350_000, 210_000, "AB12345"],
    ["Volvo", "XC60", 2019, 650_000, 380_000, "CD67890"],
    ["Tesla", "model 3", 2021, 470_000, 320_000, "EL34875"],
    ["VW", "Golf",2015, 320_000, 95_000, "GH87654"]
    ]
#merke = input("Merke: ").strip()
#modell = input("Modell: ").strip()
#aarsmodell = input("Årsmodell: ").strip()
#nypris = input("Nypris: ").strip()
#naapris= input("Nåpris: ").strip()
#regnr = input("Registreingsummer: ").strip()

merke = "Toyota" 
modell = "Yaris" 
aarsmodell = "2022" 
nypris = "350000" 
naapris= "210000" 
regnr = "AB12345" 

if merke == "":
    print("Du må skrive merke")
    exit()
if modell == "":
    print("Du må skrive modell")
    exit()
if not aarsmodell.isdigit():
    print("Du må skrive et årstall")
    exit()
else:
    aarsmodell= int(aarsmodell)
    if  not (1900<=aarsmodell<=2026):
        print("Du må skrive et gyldig årstall mellom 1900 og 2026")
        exit()
if not nypris.isdigit():
    print("Du må skrive en gdlig nypris")
    exit()
nypris = int(nypris)
if not naapris.isdigit():
    print("Du må skrive en gdlig naapris")
    exit()
naapris = int(naapris)


print(  f"Du har registert:\n"
        f"{merke} {modell} ({aarsmodell}), reg.nr: {regnr}\n"
        f"Nypris: {nypris} kr, Nåpris: {naapris} kr\n"
        f"Bilen er {2026-int(aarsmodell)} år gammel.")

if nypris > naapris:
    print(f"Bilen har sunket med {round(((nypris - naapris) / nypris)*100)}%")
else:    
    print(f"Bilen har steget med {round(((naapris - nypris)/ nypris)*100)}%")

biler.append([merke, modell, aarsmodell, nypris, naapris, regnr])

#print(biler)

bilparkVerdi = 0
for bil in biler:
    bilparkVerdi += bil[4]
print(f"Oppsummering:\n"
      f"Bilparken har en verdi på {bilparkVerdi} kroner\n"
      f"med en gjennmsnittspris på {round(bilparkVerdi/len(biler))} kroner pr bil.")
