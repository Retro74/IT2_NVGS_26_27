overskifter = ["Merke","Modell","Årsmodell","Nypris","Nåpris","Regnr"]
biler = [
    ["Toyota", "Yaris", 2022, 350_000, 210_000, "AB12345"],
    ["Volvo", "XC60", 2019, 650_000, 380_000, "CD67890"],
    ["Tesla", "Model 3", 2021, 470_000, 320_000, "EL34875"],
    ["VW", "Golf",2015, 320_000, 95_000, "GH87654"]
    ]

while True:
    if "n" == input("Vil du registere en ny bil (j/n)? "):
        break
    merke = input("Merke: ").strip()
    modell = input("Modell: ").strip()
    aarsmodell = input("Årsmodell: ").strip()
    nypris = input("Nypris: ").strip()
    naapris= input("Nåpris: ").strip()
    regnr = input("Registreringsummer: ").strip() 
    
    if merke == "":
        print("Du må skrive merke")
        continue
    if modell == "":
        print("Du må skrive modell")
        continue
    if not aarsmodell.isdigit():
        print("Du må skrive et årstall")
        continue
    else:
        aarsmodell= int(aarsmodell)
        if  not (1900<=aarsmodell<=2026):
            print("Du må skrive et gyldig årstall mellom 1900 og 2026")
            continue
    if not nypris.isdigit():
        print("Du må skrive en gyldig nypris")
        continue
    nypris = int(nypris)
    if not naapris.isdigit():
        print("Du må skrive en gyldig naapris")
        continue
    naapris = int(naapris)
    bilfunnet = False
    for bil in biler:
        if regnr == bil[-1]:
            print("Bilen er allerede registert.")
            bilfunnet = True
            continue
    if bilfunnet:
        continue
    print(  f"Du har registert:\n"
            f"{merke} {modell} ({aarsmodell}), reg.nr: {regnr}\n"
            f"Nypris: {nypris} kr, Nåpris: {naapris} kr\n"
            f"Bilen er {2026-int(aarsmodell)} år gammel.")

    if nypris > naapris:
        print(f"Bilen har sunket med {round(((nypris - naapris) / nypris)*100)}%")
    else:    
        print(f"Bilen har steget med {round(((naapris - nypris)/ nypris)*100)}%")

    biler.append([merke, modell, aarsmodell, nypris, naapris, regnr])

inputTekst = ""
for num, overskrift in enumerate(overskifter, start=1):
    inputTekst += (f"{num}) {overskrift} ")

sortValg= int(input(inputTekst + f"\nVelg sortering 1-{len(overskifter)}: "))-1

if type(biler[0][sortValg])==int:
    biler.sort(key=lambda biler: biler[sortValg], reverse=True)
else:
    biler.sort(key=lambda biler: biler[sortValg].lower())

#print(biler)
for overskrift in overskifter:
    print(f"|{overskrift:11}", end="")
print("|")

bilparkVerdi = 0
for bil in biler:
    print(f"|", end="")
    for verdi in bil:
        print(f"{verdi:11}|", end="")
    print()
    bilparkVerdi += bil[4]
    
print(f"\n"
      f"Oppsummering:\n"
      f"Bilparken har en verdi på {bilparkVerdi} kroner\n"
      f"med en gjennmsnittspris pr bil på {round(bilparkVerdi/len(biler))} kroner")