from bildatabase import biler
from bildatabase import overskrifter

print("a) Alle Toyota som er i databasen, og hvor mange det er")
toyota_biler = [toyota for toyota in biler if toyota[0].lower()=="toyota"]
for overskrift in overskrifter:
    print(f" {overskrift:9}", end="")
print()
for toyota in toyota_biler:
    for verdi in toyota:
        print(f" {verdi:8} ", end= "")
    print()
print(f"Det er {len(toyota_biler)} Toyota registrert i databasen")


print("b) Alle Toyota, nyere enn 2022 som er i databasen, og hvor mange det er")
toyota_biler = [toyota for toyota in biler if toyota[0].lower()=="toyota" and toyota[2]>2022]
for overskrift in overskrifter:
    print(f" {overskrift:9}", end="")
print()
for toyota in toyota_biler:
    for verdi in toyota:
        print(f" {verdi:8} ", end= "")
    print()
print(f"Det er {len(toyota_biler)} Toyota nyere enn 2022 registrert i databasen")


print("c) Biler under 100.000")
biler_under_100_000 = [bil for bil in biler if bil[4]<100_000]
for overskrift in overskrifter:
    print(f" {overskrift:9}", end="")
print()
for bil in biler_under_100_000:
    for verdi in bil:
        print(f" {verdi:8} ", end= "")
    print()
print(f"Det er {len(biler_under_100_000)} biler til under 100.000")



print("d) Biler med 90 % tap")
biler_under_90_tap = [bil for bil in biler if (bil[3] - bil[4])/bil[3]>0.9]
for overskrift in overskrifter:
    print(f" {overskrift:9}", end="")
print()
for bil in biler_under_90_tap:
    for verdi in bil:
        print(f" {verdi:8} ", end= "")
    print()
print(f"Det er {len(biler_under_90_tap)} biler til med 90 % tap.")


print("e) under 350.000 nyere enn 2019")
biler_under_350_nyere_2019 = [bil for bil in biler if bil[4]<350_000 and bil[2]>2019]
#Sorterer på det listen skal sorteres etter sist
biler_under_350_nyere_2019.sort(key=lambda biler_under_350_nyere_2019: (biler_under_350_nyere_2019[-1]))
#Sorterer på det listen skal sorteres etter nest-sist
biler_under_350_nyere_2019.sort(key=lambda biler_under_350_nyere_2019: (biler_under_350_nyere_2019[1]))
#Sorterer på det listen skal sorteres etter nest-først
biler_under_350_nyere_2019.sort(key=lambda biler_under_350_nyere_2019: (biler_under_350_nyere_2019[0]))
#Sorterer på det listen skal sorteres etter først
biler_under_350_nyere_2019.sort(key=lambda biler_under_350_nyere_2019: (biler_under_350_nyere_2019[2]), reverse=True)
for overskrift in overskrifter:
    print(f" {overskrift:9}", end="")
print()
for bil in biler_under_350_nyere_2019:
    for verdi in bil:
        print(f" {verdi:8} ", end= "")
    print()
print(f"Det er {len(biler_under_350_nyere_2019)} biler under 350.000 nyere enn 2019.")


print("e) Tesla hvis de er billigere enn 500.000 og Volvo-er nyere enn 2020.")
billig_tesla_el_ny_Volvo = [bil for bil in biler if (
    bil[0]=="Tesla" and bil[4]<500_000) or
    bil[0]=="Volvo" and bil[2]>2020]
for overskrift in overskrifter:
    print(f" {overskrift:9}", end="")
print()
for bil in billig_tesla_el_ny_Volvo:
    for verdi in bil:
        print(f" {verdi:8} ", end= "")
    print()
print(f"Det er {len(billig_tesla_el_ny_Volvo)} Tesla billigere enn 500.000 og Volvo-er nyere enn 2020.")
