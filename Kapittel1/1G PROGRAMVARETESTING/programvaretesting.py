from math import isclose
def addisjon(a,b):
    return a+b

print(addisjon(0.1,0.2))

def programvaretest():
    assert addisjon(2,3)==5, "Feil med addisjon av 2+3, blir ikke 5"
    assert addisjon(0,0)==0,  "Feil med addisjon av 0+0, blir ikke 0"
    assert addisjon(-10,-10)==-20,  "Feil med addisjon av -10+(-10), blir ikke -20"
    assert addisjon(0.3,0.2)==0.5,  "Feil med addisjon av 0,3+0,2, blir ikke 0,5"
    assert addisjon(2,3)!= 10, "Feil med addisjon 2+3 blir 10!"
    # Denne asserten under vil feile, 
    # derfor må vi bruke den under med isclose()
    # assert addisjon(0.1, 0.2)==0.3, "Feil med addisjon av 0.1 + 0.2 blir ikke 0.3"
    assert isclose(0.1+0.2, addisjon(0.1, 0.2)), "Feil med addisjon av 0.1 + 0.2 blir ikke 0.3"

programvaretest()
