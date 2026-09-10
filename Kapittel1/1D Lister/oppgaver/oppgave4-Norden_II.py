norden_land =["Norge", "Sverige", "Danamerk"]
norden_hovedsteder =["Oslo", "Stockholm", "Kjøbenhavn"]
norden_befolkning = [5.3, 10.2, 5.8]
norden_areal = [324000, 450000, 43000]
norden_vekstfaktor = [1.0031, 1.0034, 1.0033]
norden_sum_befolkning =0

    
while True:
    if "n" == input("Vil du legge til et land i Norden? (j/n)"):
        break
    nyttland = input("Landets navn: ")
    if nyttland in norden_land:
        print("Landet finnes allerede")
        continue
    norden_land.append(nyttland)
    norden_hovedsteder.append(input("Landets hovedstad: "))
    norden_befolkning.append(float(input("Landets befolkning: ")))
    norden_areal.append(int(input("Landets størrelse i 1000 kvadrat km: "))*1000)


print(f"|{'Land':15}|{'Hovedstad':15}|{'Befolkn.i mill':15}|")
for i in range(len(norden_land)):
    print(f"|{norden_land[i]:15}|"
          f"{norden_hovedsteder[i]:15}|"
          f"{norden_befolkning[i]:15}|")
    norden_sum_befolkning+=norden_befolkning[i]

print(f"|{'Sum':31}|{round(norden_sum_befolkning,1):15}|")