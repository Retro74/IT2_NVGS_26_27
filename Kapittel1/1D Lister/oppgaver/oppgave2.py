
alfabetet="abcdefghijklmnopqrstuvwxyzæøå"

melding=input("Skriv en melding du vi krypetere: ")
shiftcipher = int(input("Hvor mange posisjoner skal vi forskyv med? "))

krypterMelding =""
for tegn in melding:
    if tegn.lower() in alfabetet:
        krypterMelding+=alfabetet[alfabetet.index(tegn.lower())+shiftcipher]
    else:
        krypterMelding+=tegn

print(krypterMelding)