for rad in range(1,4):
    print(f"|", end="")
    for kolonne in ["A","B","C"]:
        print(f"{rad}:{kolonne}",end="|")
    print()



fornavn_elever = ["Ola", "Per", "Eli", "Pål"]
etternavn_elever = ["Olsen", "Pedersen", "Mikkelsen", "Hansen"]
fodselsaar_elever = [1999, 1998, 2001, 2009]

for fornavn, etternavn, fodselsaar in zip(fornavn_elever, etternavn_elever, fodselsaar_elever):
    print(fornavn, etternavn, fodselsaar)

