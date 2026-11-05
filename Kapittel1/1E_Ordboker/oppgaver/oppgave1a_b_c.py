handlekurv = {
  "melk": 17.90,
  "smør": 38.90,
  "kokt skinke": 23.10,
  "sjokolade": 11.90,
  "oppvaskmiddel": 24.40,
  "frossenpizza": 29.90
}

billigst_vare = min(handlekurv, key=handlekurv.get)
print(f'a) Den billigste varen er: '
      f'{billigst_vare.capitalize()}'
      f' som koster {handlekurv[billigst_vare]} kroner')
dyreste_vare = max(handlekurv, key=handlekurv.get)
print(f'b) Den dyreste varen er: '
      f'{dyreste_vare.capitalize()}'
      f' som koster {handlekurv[dyreste_vare]} kroner')
sum_varer = sum(handlekurv.values())
print(f'c) Summen av varene er: '
      f'{sum_varer:.2f} kroner')

