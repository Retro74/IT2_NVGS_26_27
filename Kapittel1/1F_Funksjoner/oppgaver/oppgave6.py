def my_encryption(bokstav, shiftcipher):
    bokstav= bokstav.lower()
    alfabetet = "abcdefghijklmnopqrstuvwxyzæøå"
    if bokstav in alfabetet:
        returtegn = alfabetet[(alfabetet.find(bokstav)+shiftcipher)%len(alfabetet)]
        return returtegn,alfabetet.find(returtegn) 
    else:
        return  bokstav, shiftcipher

def my_decryption(bokstav, shiftcipher):
    bokstav= bokstav.lower()
    alfabetet = "abcdefghijklmnopqrstuvwxyzæøå"
    if bokstav in alfabetet:
        returtegn = alfabetet[(alfabetet.find(bokstav)-shiftcipher)%len(alfabetet)]
        return returtegn,alfabetet.find(bokstav) 
    else:
        return  bokstav, shiftcipher


melding = "min hemmelige melding for denne sommeren er er erererer"
shiftcipher = 3
kryptert_melding = ""
for bokstav in melding:
    nestebokstav, shiftcipher = my_encryption(bokstav,shiftcipher)
    kryptert_melding+= nestebokstav

print(kryptert_melding)


shiftcipher = 3
dekryptertMelding =""
for bokstav in kryptert_melding:
    dekyptertTegn,shiftcipher = my_decryption(bokstav,shiftcipher)
    dekryptertMelding+=dekyptertTegn
print(dekryptertMelding)