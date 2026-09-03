biler = [
    ["Volkswagen", "Golf", "Passat", "ID.4"],
    ["Toyota", "Corolla", "Yaris", "RAV4"],
    ["Tesla", "Model 3", "Model Y", "Model S"]
]

while True:
    print("\nBilmerker:")
    for nr, merke in enumerate(biler, start=1):
        print(f"{nr}. {merke[0]}")

    valg = input(
        "\nVelg (L)egg til modell, (F)jern modell eller (A)vslutt: "
    ).upper()

    if valg == "A":
        break

    merke_nr = int(input("Velg bilmerke: ")) - 1

    if valg == "L":
        ny_modell = input("Skriv inn ny modell: ")
        biler[merke_nr].append(ny_modell)
        print("Modellen er lagt til.")

    elif valg == "F":
        print("\nModeller:")
        for modell in biler[merke_nr][1:]:
            print("-", modell)

        modell = input("Hvilken modell vil du fjerne? ")

        if modell in biler[merke_nr]:
            biler[merke_nr].remove(modell)
            print("Modellen er:")
            print("Fant ikke modellen.")

    print("\nOppdatert liste:")
    for merke in biler:
        print(f"{merke[0]}: {', '.join(merke[1:])}")