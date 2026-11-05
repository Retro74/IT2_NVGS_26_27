def sammenlign(f_tall1,f_tall2):
    if f_tall1 > f_tall2:
        return ">"
    elif f_tall1 < f_tall2:
        return "<"
    else:
        return "="

tall1 = int(input("Skriv inn tall nr 1: "))
tall2 = int(input("Skriv inn tall nr 2: "))
print(f"{tall1} {sammenlign(tall1, tall2)} {tall2}")