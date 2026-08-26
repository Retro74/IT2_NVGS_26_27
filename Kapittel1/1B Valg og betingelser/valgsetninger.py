## One-liner if

poeng = 30
resulat = "Bestått" if poeng > 50 else "Ikke bestått"

tall1 = 30
tall2 = 33

storst = tall1 if tall1 > tall2 else tall2

#Vanlig if

alder = int(input("Din alder: "))
#if alder >= 18:
#    print("Du kan ta førerprøven")
#elif alder >= 16:
#    print("Du kan starte øvelseskjøring")
#else:
#    print("Du må vente til du er til du er 16")
#

#Nøstede if-setninger
#har_traffikaltgrunnkurs = True if input("Har du grunnkurs? (j/n)")=="j" else False
#if alder >= 16:
#    if har_traffikaltgrunnkurs:
#        print("Du kan øvelseskjøre")
#    else:
#        print("Du må ta grunnkurset først")
#else:
#    print("Du må vente")

# alder mellom to verdier
if 18 < alder < 23:
    print("Du er på toppen av livet!")

valg = int(input("Velg et tall mellom 1-5: "))

#Match case
match valg:
    case 1:
        print("Du valgte alt en")
    case 2:
        print("Du valgte alt to")
    case 3:
        print("Du valgte alt tre")
    case 4:
        print("Du valgte alt fire")
    case 5:
        print("Du valgte alt fem")
    case _:
        print("Du skrev noe ukjent")