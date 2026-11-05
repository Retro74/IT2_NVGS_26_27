def fjerntallover10(f_tall_liste):
    return [tall for tall in f_tall_liste if tall <= 10]
tall_liste = [1,45,2,56,2,4,12,4,4,11,15,6]

print(fjerntallover10(tall_liste))