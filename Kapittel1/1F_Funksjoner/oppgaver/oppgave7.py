def norsk_setning_fra_liste(f_liste):
    returmelding = ""
    for i in range(len(f_liste)):
        if i == len(f_liste)-2:
            returmelding += f_liste[i] + " og "
        elif (i==len(f_liste)-1):
            returmelding += f_liste[i]
        else:
            returmelding += f_liste[i] + ", "
    return returmelding
minefavorittfilmer = ["Matrix", "Titanic", "Pulp Fiction", "Parasite"]
#print(f"Mine favorittfilmer er {norsk_setning_fra_liste(minefavorittfilmer)}.")