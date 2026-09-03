fornavn = "Roger"
a = "Roger" #Ikke gode variabel-navn 
b = "Mikalsen"
alder = 52
x = 52 #Ikke gode variabel-navn 
test = "Norge" #Ikke gode variabel-navn 
promp = 2026 #Ikke gode variabel-navn 

er_gift = True
erGift = True

#"Konstanter" i Python
ANT_DAGER_I_UKEN = 7
HOVEDSTAD = "Oslo"

sum_poeng =0

tall = int("3")
tall_tekst = str(3)

bolskverdi = bool("") #Gir False
bolskverdi = bool(0) #Gir False
bolskverdi = bool(None) #Gir False
bolskverdi = bool([]) #Gir False
# Alle andre gir True, også:
bolskverdi = bool("False") #Gir True

# Tilordning og endring av variabler
navn = "Ronny"
print(navn)
navn = "Roger"
print(navn)
navn += " Sæterlid"
navn += " Mikalsen"
print(navn)

alder = 52
print(f"{navn} er {alder} år.")
alder +=1  #Noen språk kan bruke alder++
print(f"{navn} er nå {alder} år.")
alder -=2
print(f"{navn} er nå {alder} år.")

alder *=2
print(f"Lever {navn} dobbelt så lenge blir han {alder} år.")
alder=52
alder /=2
print(f"Halveis så langt var {navn}, {alder} år.")

