skandinavia_land =["Norge", "Sverige", "Danamerk"]
skandinavia_hovedsteder =["Oslo", "Stockholm", "Kjøbenhavn"]
skandinavia_befolkning = [5.3, 10.2, 5.8]
skandinavia_areal = [324000, 450000, 43000]
skandinavia_vekstfaktor = [1.0031, 1.0034, 1.0033]
skandinavia_sum_befolkning =0
print(f"|{'Land':15}|{'Hovedstad':15}|{'Befolkn.i mill':15}|{'Estim.befolkn.2050':20}|")
for i in range(len(skandinavia_land)):
    print(f"|{skandinavia_land[i]:15}|"
          f"{skandinavia_hovedsteder[i]:15}|"
          f"{skandinavia_befolkning[i]:15}|"
          f"{round(skandinavia_befolkning[i]*skandinavia_vekstfaktor[i]**31,2):20}|")
    skandinavia_sum_befolkning+=skandinavia_befolkning[i]

print(f"|{'Sum':31}|{round(skandinavia_sum_befolkning,1):15}|")
    
for valgnr, land in enumerate(skandinavia_land, start=1):
    print(valgnr, land)
valgtLand = int(input("Hvilket land vil du se på?"))-1
print(  f"{skandinavia_land[valgtLand]}"
        f" har hovedstaden: {skandinavia_hovedsteder[valgtLand]}"
        f" og har {skandinavia_befolkning[valgtLand]} mill. mennesker"
        f" befolkningstettheten er {round((skandinavia_befolkning[valgtLand]*1_000_000)/skandinavia_areal[valgtLand])} pers. pr. kvad.km")