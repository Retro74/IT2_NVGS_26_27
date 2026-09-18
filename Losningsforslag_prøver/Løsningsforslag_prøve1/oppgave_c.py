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

print(  f"Du har reistert:\n"
        f"{merke} {modell} ({aarsmodell}), reg.nr: {regnr}\n"
        f"Nypris: {nypris} kr, Nåpris: {naapris} kr\n"
        f"Bilen er {2026-int(aarsmodell)} år gammel.")