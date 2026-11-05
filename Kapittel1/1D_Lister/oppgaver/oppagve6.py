biler_merke_modell =[
    ["Volvo","XC90", "ex40", "ex60"],
    ["Nissan", "Ariya", "X-trail", "Qashqai"], 
    ["Toyota", "Rav4", "Corolla"], 
    ["Tesla", "Model 3", "Model Y", "Model X"]]

for merke in biler_merke_modell:
    print("Merke: ", end="")
    for bil in merke:
        print(bil)
    print()