

#Definerer en liste

bilmerker = ["Toyota", "VW", "Tesla"]
#print(bilmerker[1])
#print(bilmerker[0:2])
bilmerker[0] ="Volvo"
#print(bilmerker)
bilmerker.append("Toyota")
#print(bilmerker)
bilmerker.insert(0,"Audi")
#print(bilmerker)

bilmerker.extend(["Mini", "BMW"])
#print(bilmerker)

##Fjerne
#bilmerker.remove("Mini")
#print(bilmerker)
#fjernet_merke = bilmerker.pop(3)
#print(bilmerker, "Vi fjernet", fjernet_merke)


#print(bilmerker)
#print(*bilmerker)
#teller = 1
#for nr, bil in enumerate(bilmerker, start=1):
#    print(nr, bil)

#finnMerke = input("Hvilket bilmerke skal vi finne? ").capitalize()
#if finnMerke in bilmerker:
#    print(f"Ja vi har registert {finnMerke}")
#else:
#    print(f"Nei, {finnMerke} er ikke registert")

#tilbakemelding = f"Fant ikke bilmerke {finnMerke}"
#for bilmerke in bilmerker:
#    if bilmerke.lower() == finnMerke.lower():
#        tilbakemelding = f"Fant bilmerket {finnMerke}"
#        break

#print(tilbakemelding)






priser = [299, 699, 89, 299, 33, 345, 299, 33, 33]
print(f"Summen av priser er: {sum(priser)}")
print(f"Den høyeste prisen er: {max(priser)}")
print(f"Den laveste prisen er: {min(priser)}")

import statistics as st
print(f"Gjennomsnittsprisen er: {st.mean(priser)}")
print(f"Medianen er: {st.median(priser)}")
print(f"Typetallet er: {st.mode(priser)}")



#Sortering
#priser.sort() #Sorterer selve listen
#Kopi av listen og sorterer den
sorterte_priser = sorted(priser)
print(priser)
print(sorterte_priser)
sorterte_priser.reverse()
print(sorterte_priser)

unik_prisliste = sorted(set(sorterte_priser))
print(unik_prisliste) 


from statistics import mean
uketemperaturer = input("Skriv inn ukens temperaturer (kommaseparert): ")
uketemperaturer = uketemperaturer.split(",")
print(uketemperaturer)

#Enten:
#for i in range(len(uketemperaturer)):
#    uketemperaturer[i] = int(uketemperaturer[i]) 

#Eller:
uketemperaturer = [int(temperatur) for temperatur in uketemperaturer]
print(f"Gjennomsnittstemepraturen er: {mean(uketemperaturer)}")





bilmerker = [
    'Audi', 
    'Volvo', 
    'VW', 
    'Tesla', 
    'Toyota', 
    'Mini', 
    'BMW'
    ]
