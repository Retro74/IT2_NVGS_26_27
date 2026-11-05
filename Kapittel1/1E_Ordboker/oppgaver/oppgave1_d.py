handlekurv = {
  "melk": {"enhetspris": 17.90, "antall": 3},
  "smør": {"enhetspris": 38.90, "antall": 2},
  "kokt skinke": {"enhetspris": 23.10, "antall": 1},
  "sjokolade": {"enhetspris": 11.90, "antall": 2},
  "oppvaskmiddel": {"enhetspris": 24.40, "antall": 1},
  "frossenpizza": {"enhetspris": 29.90, "antall": 3},
}

#Bruker dictionary comprehention til å hente ut alle verdiene fra hoved-ordboken. 
# og bruker verdiene:
#{'enhetspris': 17.9, 'antall': 3}
#{'enhetspris': 38.9, 'antall': 2}
#...
samlet_sum = sum(vare["enhetspris"] * vare["antall"] for vare in handlekurv.values())

print(f'd) Summen av varene er: '
      f'{samlet_sum:.2f} kroner')
