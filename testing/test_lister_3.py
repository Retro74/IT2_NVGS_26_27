modeller = ["Model 3", "Golf", "Model Y", "Passat"]

for modell in modeller[::-1]:
    if modell.startswith("Model"):
        modeller.remove(modell)

print(modeller)
