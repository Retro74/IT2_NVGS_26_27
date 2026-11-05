def legg_sammen(f_tall1, f_tall2):
    return f_tall1+ f_tall2

tall1 = int(input("Skriv inn tall nr 1: "))
tall2 = int(input("Skriv inn tall nr 2: "))
tall3 = int(input("Skriv inn tall nr 3: "))

print(f"{tall1} + {tall2} + {tall3} = {legg_sammen(legg_sammen(tall1, tall2), tall3)}")