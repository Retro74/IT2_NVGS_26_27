def rensliste(f_liste, f_nedre_grense, f_ovre_grense):
    return [x for x in f_liste if f_nedre_grense<x<f_ovre_grense]

liste = [3,5,62,6,3,6,8,57,5,3,53,2,11,46,14,25,25,33,57,25,2,45,7,34,61,1,2,8,19]
nedre_grense = 10
ovregrense = 40

print(f"Renset liste: {rensliste(liste, nedre_grense, ovregrense)}")