def si_hei(navn):
    return f"Hei {navn}"


#print(si_hei("Ola"))
#try: 
#    print(si_hei())
#except TypeError as err:
#    print(f"Feilmelding: {str(err)}")


#def hilsning(navn, alder , bosted="ukjent", land="Norge"):
#    if bosted == "ukjent":
#        print(f"Hei, jeg er {navn} og bor i {land}")
#    else:        
#        print(f"Hei, jeg er {navn}, og kommer fra {bosted}, {land} og er {alder}")

#hilsning(navn="Roger", alder=52, bosted= "Harstad")
#ilsning("Ola", 33, land="Sverige")


#x, y = 22, 45
#print("x:", x)
#print("y:", y)

def max_og_min(tallrekke):
    return max(tallrekke), min(tallrekke)

minetall =[4,2,6,8,3,6,8,2,1,76,8,4,]
#print(type(max_og_min(minetall)))

mittstorstetall, mittminstetall = max_og_min(minetall)
#print(max_og_min(minetall))
#print(mittminstetall)
#print(mittstorstetall)
#alder = 18
#def test():
#    #alder = 17
#    print(f"Inne i funkjsonen er variabelen alder = {alder}")

#test()
#print(f"Utenfor  funkjsonen er variabelen alder = {alder}")

import copy
minliste = [1,2,3]
def endreliste(f_minliste):
    f_minliste[0]=7
    #print(f_minliste)

#print(minliste)
endreliste(minliste)
#endreliste(minliste.copy())
#print(minliste)

def summer(*tall):
    print(type(tall))
    return sum(tall)

#minsum = summer(4,6,2,7,4,2,8,9)
#print(minsum)

def visinfo(*navn): # *args
    if not navn:
        print("Ingen ting å vise")
        return
    for enkeltnavn in navn:
        print(enkeltnavn)

#visinfo("Anna", "Ola", "Nils")
#visinfo()

def skrivUtInfo(**info): #**kwargs
#    print(type(info))
    for nokkel, verdi in info.items():
        print(f"{nokkel}: {verdi}")
#    print(info)

#skrivUtInfo(fornavn="Roger", alder=52, bosted="Nesoddtangen")





def elevinfo(
        fornavn, etternavn, klasse, #Vanlige argumenter
        *fag,                       #Posisjonelle argumenter 
        skole="Nesodden vgs",       #Navngitte argument med standardverdier
        epost = None, 
        **annen_info,                #Ekstra navngitte argument
        ):
    while not fag:
        fag = (input("Eleven har ingen fag. Skriv inn et fag: "))
    print(f"Navn:{fornavn} {etternavn} går i {klasse} ved {skole}")
    print(f"Fag: {fag}")
    if epost:
        print(f"Epost: {epost}")
    print(f"Annet informajson: {annen_info}")

#elevinfo("Ola","Olsen", "1STA", "IT-1", "Kjemi 1", "R1", "Norsk", alder=17, epost="olao@afk.no")

#elevinfo("Eli", "Nilsen", "2STC", alder=18, skole="Frogn vgs")


def areal(l, b):
    return l*b

def pris_pr_kvm(enhetspris, l, b):
    return enhetspris*areal(l,b)

lengde = 4
bredde = 3.5
enhetspris= 399
pris = pris_pr_kvm(enhetspris, lengde, bredde)
print(f"Pris: {pris:.2f} kroner.")

