skandinavia = [
["Norge", "Oslo", 5.3, 324000, 1.0031],
["Sverige", "Stockholm", 10.2, 450000, 1.0034],
["Danmark", "Kjøbenhavn", 5.8, 43000, 1.0033]
]
skandinavia_sum_befolkning =0

    
print(f"|{'Land':15}|{'Hovedstad':15}|{'Befolkn.i mill':15}|")
for land in skandinavia:
    print(f"|{skandinavia_land[i]:15}|"
          f"{skandinavia_hovedsteder[i]:15}|"
          f"{skandinavia_befolkning[i]:15}|")
    skandinavia_sum_befolkning+=skandinavia_befolkning[i]

print(f"|{'Sum':31}|{round(skandinavia_sum_befolkning,1):15}|")