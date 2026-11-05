from math import sqrt
from oppgave7 import norsk_setning_fra_liste
def er_primtall(n):
    if n < 2:
        return False
    for divisor in range(2, int(sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True

def primtall_i_intervall(start, slutt):
    primtall = []
    for tall in range(start, slutt + 1):
        if er_primtall(tall):
            primtall.append(tall)
    return primtall

print("Hvor skal vi lete etter primtall?")
nedregrense = int(input("Nedre grense: "))
ovregrense = int(input("Øvre grense: "))
#print(f"Primtallene mellom {nedregrense} og {ovregrense} er {primtall_i_intervall(nedregrense,ovregrense)}.")
#Bedre norsk med import av denne funksjonen fra oppgave 7
print(f"Primtallene mellom {nedregrense} og {ovregrense} er {norsk_setning_fra_liste([str(verdi) for verdi in primtall_i_intervall(nedregrense,ovregrense)])}.")